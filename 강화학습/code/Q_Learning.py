# Library
import numpy as np
import random

# Grid world
grid_size = 4
num_states = grid_size * grid_size
num_actions = 4

# action 
## 0 : 위, 1 : 아래, 2 : 왼쪽, 3 : 오른쪽

goal_state = 15
trap_state = 5

q_table = np.zeros((num_states, num_actions))

# 학습율
alpha = 0.1 
# 할인율
gamma = 0.99
# 탐험 비율
epsilon = 0.1
episodes = 1000
max_steps = 100

# 상태 -> 좌표
def state_to_pos(state):
    row = state // grid_size
    col = state % grid_size
    return row, col

# 좌표 -> 상태
def pos_to_state(row, col):
    return row * grid_size + col

def step(state, action):
    # 현재 상태
    row, col = state_to_pos(state)

    if action == 0:
        row -= 1
    elif action == 1:
        row += 1
    elif action == 2:
        col -= 1
    elif action == 3:
        col += 1
    
    row = np.clip(row, 0, grid_size - 1)
    col = np.clip(col, 0, grid_size - 1)

    next_state = pos_to_state(row, col)

    if next_state == goal_state:
        reward = 1
        done = True
    elif next_state == trap_state:
        reward = -1
        done = True
    else:
        reward = -0.01
        done = False
    
    return next_state, reward, done

# Train Q-Learning
for episode in range(episodes):

    state = 0

    for step_idx in range(max_steps):

        # Epsilon-Greedy action 
        ## 탐험
        if random.random() < epsilon:
            action = random.randint(0, num_actions - 1)
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done = step(state, action)

        # Q-Learning update
        best_next_q = np.max(q_table[next_state])

        q_table[state, action] = q_table[state, action] + alpha * (reward + gamma * best_next_q - q_table[state, action])

        state = next_state 

        if done:
            break 

print(q_table)

state = 0
path = [state]

for _ in range(20):

    action = np.argmax(q_table[state])
    next_state, reward, done = step(state, action)

    path.append(next_state)
    state = next_state

    if done:
        break

print("Path:", path)


