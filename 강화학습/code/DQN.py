# Library
import random
from collections import deque

import gymnasium as gym
import numpy as np
import torch
from torch import nn
from torch import optim

# Q-Network
class DQN(nn.Module):

    def __init__(self, state_dim, action_dim):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128,128),
            nn.ReLU(),
            nn.Linear(128,action_dim)
        )

    def forward(self, x):
        return self.net(x)

# 반복 저장소
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
    
    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        return np.array(states), np.array(actions), np.array(rewards), np.array(next_states), np.array(done)

    def __len__(self):
        return len(self.buffer)

# 초매개변수
env_name = 'CartPole-v1'
gamma = 0.99
lr = 1e-3
buffer_size = 10000
batch_size = 64
eps_start = 1
eps_end = 0.01
eps_decay = 0.995
target_update = 10
num_episodes = 500

# 장치
device = torch.device('cuda')

# 환경
env = gym.make(env_name)

# 상태 차원
state_dim = env.observation_space.shape[0]
# 행동 개수
action_dim = env.action_space.n

# 정책 신경망. 실제 학습되는 신경망
policy_net = DQN(state_dim, action_dim).to(device)
# 목표 신경망
target_net = DQN(state_dim, action_dim).to(device)

target_net.load_state_dict(policy_net.state_dict())

target_net.eval()

# Optimizer
optimizer = optim.Adam(policy_net.parameters(), lr=lr)

# 반복 저장소 생성
replay_buffer = ReplayBuffer(buffer_size)

# Initial epsilon
epsilon = eps_start 

# Epsilon-Greedy action
def select_action(state):

    global epsilon

    # 탐험
    if random.random() < epsilon:
        return env.action_space.sample()

    state = torch.FloatTensor(state).unsqueeze(0).to(device)

    with torch.no_grad():
        q_values = policy_net(state)

    return q_values.argmax().item()

# 학습 함수
def train_step():
    # Buffer data가 부족하면 학습 X
    if len(replay_buffer) < batch_size:
        return 

    states, actions, rewards, next_states, dones = replay_buffer.sample(batch_size)
    states = torch.FloatTensor(states).to(device)
    actions = torch.LongTensor(actions).unsqueeze(1).to(device)
    rewards = torch.as_tensor(rewards, dtype=torch.float32, device=device).view(-1, 1)
    next_states = torch.FloatTensor(next_states).to(device)
    dones = torch.as_tensor(dones, dtype=torch.float32, device=device).view(-1, 1)

    # 현재 Q값 계산
    current_q = policy_net(states).gather(1, actions)
    # Target Q
    with torch.no_grad():
        next_q = target_net(next_states).max(1)[0].unsqueeze(1)
        target_q = rewards + gamma * next_q * (1 - dones)

    # 손실
    loss = nn.MSELoss()(current_q, target_q)

    # 역전파
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 학습
for episode in range(num_episodes):

    # 환경 초기화
    state, _ = env.reset()
    done = False 
    total_reward = 0

    while not done:
        # 행동 선택
        action = select_action(state)
        next_state, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        # 경험 저장
        replay_buffer.push(state, action, reward, next_state, done)
        # 갱신
        state = next_state 
        total_reward += reward 

        train_step()

    epsilon = max(eps_end, epsilon * eps_decay)

    # 목표 신경망 최신화
    if episode % target_update == 0:
        target_net.load_state_dict(policy_net.state_dict())

    print(
        f"Episode {episode:4d} | ",
        f'Reward {total_reward:4.0f} | ',
        f'Epsilon {epsilon:3f}'
    )

env.close()
