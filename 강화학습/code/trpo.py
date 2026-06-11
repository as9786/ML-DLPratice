# Library
import gym
import torch
from torch import nn
from torch import optim
from torch.distributions import Categorical

# 장치
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 정책 신경망
class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.net(x)
    
    # 행동 확률을 이산 분포로 변환
    def get_dist(self, states):
        probs = self.forward(states)
        return Categorical(probs)
    
    # 특정 상태에서 특정 행동을 선택할 log probability 계산
    def get_log_prob(self, states, actions):
        dist = self.get_dist(states)
        return dist.log_prob(actions)
    
# 가치 신경망
class ValueNetwork(nn.Module):
    def __init__(self, state_dim):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)
    
# Utility function
## 모형의 가중치들을 하나의 1-D vector로 변환 
def flat_params(model):
    return torch.cat([p.data.view(-1) for p in model.parameters()])

## 하나의 1-D vector를 다시 모형 가중치 형태로 북원
def set_flat_params(model, flat_vector):
    idx = 0

    for p in model.parameters():
        # 현재 가중치의 원소 개수
        numel = p.numel()
        p.data.copy_(flat_vector[idx:idx+numel].view_as(p))
        idx += numel 

## 경사를 1차원으로
def flat_grad(grads):
    return torch.cat([g.contiguous().view(-1) for g in grads])

# 보상 계산
def compute_returns(rewards, dones, gamma=0.99):
    returns = []
    ret = 0

    for reward, done in zip(reversed(rewards), reversed(dones)):
        # Episode가 끝났을 경우
        if done:
            ret = 0
        # 할인된 보상 계산
        ret = reward + gamma * ret
        returns.insert(0, ret)
    
    return torch.tensor(returns, dtype=torch.float32).to(device)

# Advantage = 실제 보상 - 가치 신경망이 예측한 가치
def compute_advantages(returns, values):
    advantages = returns - values.detach()
    # 정규화 
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
    return advantages

# Conjugate gradient
def conjugate_gradient(avp_func, b, max_iter=10, residual_tol=1e-10):
    # 우리가 구하고자 하는 해
    x = torch.zeros_like(b)
    # 초기 잔차
    r = b.clone()
    # 탐색 방향
    p = b.clone()
    # 잔차의 크기
    r_dot_r = torch.dot(r,r)

    for _ in range(max_iter):
        avp = avp_func(p)
        # 현재 방향으로 얼마나 갈지 계산
        alpha = r_dot_r / (torch.dot(p, avp) + 1e-9)

        # 최신화
        x += alpha * p
        r -= alpha * avp

        # 새 잔차 크기 계산
        new_r_dot_r = torch.dot(r, r)

        # 잔차가 중분히 작으면 종료
        if new_r_dot_r < residual_tol:
            break
        
        # 다음 탐색 방향
        beta = new_r_dot_r / r_dot_r
        p = r + beta * p
        # 잔차 크기 갱신
        r_dot_r = new_r_dot_r

    return x

def trpo_update(policy, value_net, states, actions, old_log_probs, returns, advantages, max_kl=0.01, damping=0.1):
    # 가치 신경망 최신화
    value_optimizer = optim.Adam(value_net.parameters(), lr=1e-3)

    for _ in range(5):
        # 현재 가치 예측
        values = value_net(states)

        # MSE loss
        value_loss = ((values - returns) ** 2).mean()

        # 가치 신경망 최신화
        value_optimizer.zero_grad()
        value_loss.backward()
        value_optimizer.step()

    # Define surrogate objective. 새로운 정책이 좋은 행동의 확률을 높이면 surrogate가 증가
    def surrogate_loss():
        # 현재 정책 기준 log probability
        new_log_probs = policy.get_log_prob(states, actions)
        # 확률 비율 계산
        ratio = torch.exp(new_log_probs - old_log_probs)

        # Surrogate objective
        return (ratio * advantages).mean()
    
    # 현재 surrogate loss 계산
    loss = surrogate_loss()

    # Surrogate objective의 경사 계산
    grads = torch.autograd.grad(loss, policy.parameters())

    # To vector
    loss_grad = flat_grad(grads).detach()

    # 이전 정책 분포 저장
    with torch.no_grad():
        old_dist = policy.get_dist(states)

    # KL-Divergence
    def kl_divergence():
        # 현재 정책을 새 분포로 사용
        new_dist = policy.get_dist(states)

        # 오래된 정책의 행동 확률
        old_probs = old_dist.probs.detach()

        # 새 정책의 행동 확률
        new_probs = new_dist.probs

        # KL
        kl = (old_probs * (torch.log(old_probs + 1e-8) - torch.log(new_probs + 1e-8))).sum(dim=1)

        return kl.mean()
    
    # Hessian vector product
    def hessian_vector_product(v):
        # KL divergence
        kl = kl_divergence()

        # KL의 1차 경사 계산
        kl_grads = torch.autograd.grad(kl, policy.parameters(), create_graph=True)
        flat_kl_grads = flat_grad(kl_grads)
        kl_v = torch.dot(flat_kl_grads, v)
        kl_second_grads = torch.autograd.grad(kl_v, policy.parameters())
        flat_kl_second_grads = flat_grad(kl_second_grads).detach()

        return flat_kl_second_grads + damping * v
    
    step_dir = conjugate_gradient(hessian_vector_product, loss_grad)
    shs = 0.5 * torch.dot(step_dir, hessian_vector_product(step_dir))
    step_size = torch.sqrt(max_kl / (shs+1e-8))
    full_step = step_size * step_dir 
    old_params = flat_params(policy)
    old_loss = surrogate_loss().detach()

    # Line search
    for step_frac in [1, 0.5, 0.25, 0.125, 0.0625]:
        # 후보 모수
        new_params = old_params + step_frac * full_step
        # 정책 가중치를 후보 값으로 변경
        set_flat_params(policy, new_params)
        # 변경후 surrogate objective
        new_loss = surrogate_loss()
        kl = kl_divergence()
        # 목적 증가 확인
        improvement = new_loss - old_loss 

        # Surrogate도 증가하고, KL 제한도 만족하면 최산화
        if improvement > 0 and kl <= max_kl:
            return {'surrogate_loss' : new_loss.item(), 'kl' : kl.item(), 'accepted' : True}
        
    # Line search 실패 시 원래 가중치로
    set_flat_params(policy, old_params)

    return {'surrogate_loss' : old_loss.item(), 'kl' : kl_divergence.item(), 'accepted' : False}

def collect_trajectories(env, policy, batch_size=2048):
    states = []
    actions = []
    rewards = []
    dones = []
    log_probs = []

    # 환경 초기화
    state, _ = env.reset()

    # 배치 크기만큼 timestamp 수집
    while len(states) < batch_size:
        state_tensor = torch.tensor(state, dtype=torch.float32).to(device)

        # 현재 정책의 행동 분포 생성
        dist = policy.get_dist(state_tensor.unsqueeze(0))
        # 분포에서 행동 표본 추출
        action = dist.sample()
        # 선택한 행동의 log probability 계산
        log_prob = dist.log_prob(action)

        # 환경에 행동 적용
        next_state, reward, terminated, truncated, _ = env.step(action.item())

        done = terminated or truncated

        states.append(state)
        actions.append(action)
        rewards.append(reward)
        dones.append(done)
        log_probs.append(log_prob.item())

        # 다음 상태로
        state = next_state

        if done:
            state, _ = env.reset()

    states = torch.tensor(states, dtype=torch.float32).to(device)
    actions = torch.tensor(actions,dtype=torch.long).to(device)
    old_log_probs = torch.tensor(log_probs,dtype=torch.float32).to(device)

    return states, actions, rewards, dones, old_log_probs

# 학습
def train():
    env = gym.make('CartPole-v1')

    # 상태 차원
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n

    # 정책 신경망
    policy = PolicyNetwork(state_dim, action_dim).to(device)
    # 가치 신경망
    value_net = ValueNetwork(state_dim).to(device)
    # 할인율
    gamma = 0.99
    # TRPO KL constraint
    max_kl = 0.01

    # 학습
    for iteration in range(200):

        states, actions, rewards, dones, old_log_probs = collect_trajectories(env, policy, 2048)
        returns = compute_returns(rewards, dones, gamma)
        values = value_net(states)
        advantages = compute_advantages(returns, values)
        result = trpo_update(policy, value_net, states, actions, old_log_probs, returns, advantages, max_kl)

        # done=True 개수는 episode 개수로 볼 수 있다.
        num_episodes = max(1, sum(dones))

        # 평균 episode return
        avg_return = sum(rewards) / num_episodes

        print(
            f"Iter {iteration:03d} | "
            f"AvgReturn: {avg_return:.2f} | "
            f"KL: {result['kl']:.5f} | "
            f"Accepted: {result['accepted']}"
        )
    env.close()

if __name__ == '__main__':
    train()
