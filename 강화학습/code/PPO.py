# Library
import gymnasium as gym
import numpy as np
import torch
from torch import nn
from torch import optim
from torch.distributions import Categorical

# Actor-Critic network
class ActorCritic(nn.Module):
    '''
    Actor : 현재 상태를 보고 어떤 행동을 할 지 결정
    Critic : 현재 상태가 얼마나 좋은 상태인지 예측
    '''
    def __init__(self, state_dim, action_dim, hidden_dim=64):
        super().__init__()

        # 공통적인 특징 추출기
        self.shared = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh()
        )

        # 행동 확률 출력
        self.actor = nn.Linear(hidden_dim, action_dim)

        # 상태 가치 출력
        self.critic = nn.Linear(hidden_dim, 1)

    def forward(self, state):
        x = self.shared(state)

        logits = self.actor(x)
        value = self.critic(x)

        return logits, value

    def get_action(self, state):
        logits, value = self.forward(state)

        dist = Categorical(logits=logits)
        action = dist.sample()

        log_prob = dist.log_prob(action)

        return action, log_prob, value

    def evaluate_actions(self, states, actions):
        logits, values = self.forward(states)

        dist = Categorical(logits=logits)

        log_probs = dist.log_prob(actions)
        # Entropy : 정책의 무작위성 정도
        entropy = dist.entropy()

        return log_probs, values.squeeze(-1), entropy

def compute_gae(rewards, values, dones, next_value, gamma=0.99, lam=0.95):
    advantages = []
    gae = 0

    # 마지막 상태의 가치를 뒤에 추가
    values = values + [next_value]

    # 뒤에서부터 이점 계산
    for t in reversed(range(len(rewards))):
        mask = 1 - dones[t]

        # TD error
        delta = rewards[t] + gamma * values[t+1] * mask - values[t]

        # GAE
        gae = delta + gamma * lam * mask * gae

        advantages.insert(0, gae)

    returns = [adv + val for adv, val in zip(advantages, values[:-1])]

    return advantages, returns

# 환경 생성
env = gym.make('CartPole-v1')

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 모형
model = ActorCritic(state_dim, action_dim).to(device)

# 최적화
optimizer = optim.Adam(model.parameters(), lr=3e-4)

# Hyperparameter
gamma = 0.99
lam = 0.95
clip_eps = 0.2
value_coef = 0.5
entropy_coef = 0.01
rollout_steps = 2048
ppo_epochs = 10
mini_batch_size = 64
max_updates = 300

# 환경초기화
state, _ = env.reset()
episode_reward = 0

for update in range(1, max_updates + 1):
    states = []
    actions = []
    rewards = []
    dones = []
    log_probs = []
    values = []

    # Rollout
    for step in range(rollout_steps):
        state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)

        with torch.no_grad():
            action, log_prob, value = model.get_action(state_tensor)

        # 선택한 행동으로 단계 진행
        next_state, reward, terminated, truncated, _ = env.step(action.item())

        done = terminated or truncated

        states.append(state)
        actions.append(action.item())
        rewards.append(reward)
        dones.append(float(done))
        log_probs.append(log_prob.item())
        values.append(value.item())

        state = next_state

        episode_reward += reward

        if done:
            state, _ = env.reset()

    state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)

    with torch.no_grad():
        _, next_value = model.forward(state_tensor)
        next_value = next_value.item()

    advantages , returns = compute_gae(rewards, values, dones, next_value, gamma, lam)

    states = torch.tensor(np.array(states), dtype=torch.float32).to(device)
    actions = torch.tensor(actions, dtype=torch.long).to(device)
    old_log_probs = torch.tensor(log_probs, dtype=torch.float32).to(device)
    advantages = torch.tensor(advantages, dtype=torch.float32).to(device)
    returns = torch.tensor(returns, dtype=torch.float32).to(device)

    # Advantage 정규화
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

    dataset_size = states.size(0)

    # PPO Update
    for epoch in range(ppo_epochs):
        # 데이터 index 섞기
        indices = np.arange(dataset_size)
        np.random.shuffle(indices)

        # mini-batch 단위로 학습
        for start in range(0, dataset_size, mini_batch_size):
            end = start + mini_batch_size
            batch_idx = indices[start:end]

            # mini-batch 추출
            batch_states = states[batch_idx]
            batch_actions = actions[batch_idx]
            batch_old_log_probs = old_log_probs[batch_idx]
            batch_advantages = advantages[batch_idx]
            batch_returns = returns[batch_idx]

            # 현재 정책 기준으로 log probability, value, entropy 계산
            new_log_probs, values_pred, entropy = model.evaluate_actions(
                batch_states,
                batch_actions
            )

            # policy ratio 계산
            ratio = torch.exp(new_log_probs - batch_old_log_probs)

            # clipping 없는 objective
            unclipped = ratio * batch_advantages

            # clipping 적용한 objective
            clipped = torch.clamp(
                ratio,
                1 - clip_eps,
                1 + clip_eps
            ) * batch_advantages

            # Actor Loss
            actor_loss = -torch.min(unclipped, clipped).mean()

            # Critic Loss
            critic_loss = nn.functional.mse_loss(
                values_pred,
                batch_returns
            )

            # Entropy Loss
            entropy_loss = entropy.mean()

            # 전체 loss
            loss = (
                actor_loss
                + value_coef * critic_loss
                - entropy_coef * entropy_loss
            )

            # gradient 초기화
            optimizer.zero_grad()

            # 역전파
            loss.backward()

            # gradient clipping
            # gradient가 너무 커져서 학습이 불안정해지는 것을 방지
            nn.utils.clip_grad_norm_(
                model.parameters(),
                max_norm=0.5
            )

            # 파라미터 업데이트
            optimizer.step()

    # 로그 출력
    if update % 10 == 0:
        print(
            f"Update: {update:03d} | "
            f"Last rollout reward sum: {sum(rewards):.1f} | "
            f"Loss: {loss.item():.4f} | "
            f"Actor Loss: {actor_loss.item():.4f} | "
            f"Critic Loss: {critic_loss.item():.4f}"
        )

# 환경 종료
env.close()


