# Playing Atari with Deep Reinforcement Learning
- 지도 학습 : 입력 -> 정답
- 강화 학습 : 상태, 보상
- Conventional Q-Learning learns by storing the state-action value, Q(s,a), in a tabular format
- As the state and action spaces become larger, tabular Q-learning suffers from high memory requirements and long exploration times. DL overcomes this issue
- DL approximates the Q-table with a nonlinear Q-function parameterized by a neural network. As a result, the agent can estimate Q-values for unseen paris without storing all possible Q-values in a table

## Limitations of the before DQN
- Training instability and non-convergence
- 
