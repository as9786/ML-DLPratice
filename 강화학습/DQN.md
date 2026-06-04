# Playing Atari with Deep Reinforcement Learning
- 지도 학습 : 입력 -> 정답
- 강화 학습 : 상태, 보상
- Conventional Q-Learning learns by storing the state-action value, Q(s,a), in a tabular format
- As the state and action spaces become larger, tabular Q-learning suffers from high memory requirements and long exploration times. DL overcomes this issue
- DL approximates the Q-table with a nonlinear Q-function parameterized by a neural network. As a result, the agent can estimate Q-values for unseen paris without storing all possible Q-values in a table

## Limitations of the before DQ
- Training instability and non-convergence
- 학습 불안정성의 원인
    - 단순한 상관관계
    - Data distribution
    - Moving target value
- DQN addresses these issues by introducing experience replay and a target network

## DQN
- 구성 요소
    1. CNN
    2. Experience replay
    3. Target network

### Conventional deep Q-learning algorithm
1. 가중치 초기화. 매 단계마다 2~5 반복
2. Select action according to the epsilon-greedy policy
3. Execute action $a_t$ and observe the transition $e_t = (s_t, a_t, r_t, s_{t+1})$
4. 목표 값 계싼 : $y_t = r_t + \gamma max_{a'} Q(s_{t+1}, a';\theta)$
5. 손실 함수 최소화하는 방향으로 가중치 최신화. $(y_t - Q(s_t, a_t,;\theta))^2$

### 1. 합성곱 신경망 구조
- 인간과 유사한 형식으로 입력을 처리
- 행동을 제외한 상태만을 입력으로 받고 출력으로 행동들에 해당하는 복수개의 Q-value들을 뽑아내는 구조
