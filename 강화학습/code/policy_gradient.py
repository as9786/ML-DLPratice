# Library
import gymnasium as gym
import torch
from torch import nn
from torch import optim

# 정책 신경망
class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )

    def forward(self, x):
        logits = self.net(x)
        return torch.softmax(logits, dim=-1)

# 초매개변수
lr = 1e-3
gamma = 0.99
episodes = 1000

# 환경
env = gym.make('CartPole-v1')

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

policy = PolicyNetwork(state_dim, action_dim)
optimizer = optim.Adam(policy.parameters(), lr=lr)

# 학습
for episode in range(episodes):
    state, _ = env.reset()
    
    log_probs = []
    rewards = []

    done = False
    
    while not done:
        state_tensor = torch.FloatTensor(state)
        probs = policy(state_tensor)
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()
        next_state, reward, terminated, truncated, _ = env.step(action.item())

        done = terminated or truncated

        log_probs.append(dist.log_prob(action))
        rewards.append(reward)

        state = next_state 

    # 보상 계산
    returns = []

    g = 0

    for reward in reversed(rewards):
        g = reward + gamma * g
        returns.insert(0, g)

    returns = torch.tensor(returns)

    # 정규화
    returns = (returns - returns.mean()) / (returns.std() + 1e-8)

    # 손실
    loss = []

    for log_prob, g in zip(log_probs, returns):
        loss.append(-log_prob * g)

    loss = torch.stack(loss).sum()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if episode % 10 == 0:
        print(
            f'Episode {episode:4d} | ',
            f'Reward {sum(rewards):4.0f}'
        )

env.close()

