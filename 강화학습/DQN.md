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
- The network takes only the state as input and outputs multiple Q-values, each corresponding to a possible action
- 합성곱 신경망을 행동마다 여러 번 통과시키지 않고, 상태 입력 한 번만 합성곱 신경망에 통과시켜주면 됨
- 상태 -> 합성곱 신경망 -> [Q_left, Q_right, Q_up, Q_down]

### 2. 경험 반복

1. 매 단계마다 추출된 표본 $e_t=(s_t, a_t, r_t, s_{t+1})$을 반복 저장소(replay memory) D에 저장
2. D에 저장된 표본들을 균일하게 추출하여 학습에 이용

- 현재 선택된 행동을 수행해 결과 값과 표본을 얻지만 바로 평가에 이용하지 않고, 의도적으로 지연
- 학습 불안정성을 유발하는 요인들 제거
- 단순한 상관관계
    - DL assumes that training samples are independently drawn from the data distribution
    - 하지만 강화학습은 표본 사이에 종속성 존재
    - 왜냐하면 현재 표본에서의 정책과 상태 전환 가능성에 의해 다음 표본이 생성
    - Training on highly correlated samples can prevent the network from learning an accurate Q-funciton
- Changes in the data distribution
    - In on-policy learning, Q-value updates can change the agent's policy, which in turn alters the distribution of the training data
