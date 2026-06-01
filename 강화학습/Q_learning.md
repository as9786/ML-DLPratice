# Q-Learning

- 어떤 상태에서 어떤 행동을 해야 가장 많은 보상을 받을 수 있는지

## Q function
- 상태-행동 가치 함수
- Q(s,a)를 학습 
- 상태와 행동을 입력했을 때, 이에 대한 가치를 출력
- 내가 가진 상태랑 행동을 주면 이런 상태에서 이런 행동을 하면 얼마만큼의 보상을 받을 수 있는지 알려줌
- 이를 알게되면, 값을 최대화하는 정책을 찾으면 됨
- $\pi^* (s)=argmax_a Q(s,a)$

## How to make Q
- Q value : 상태 s에서 행동 a를 했을 때 앞으로 받을 총 보상 
- Once we know the Q-values, we can simply take actions according to the policy
- Finding the Q-valujes is also referred to as learning the Q-function
- 현재 상태에서 행동을 취하면, 상태는 변하게 됨
- 또한 보상을 받음
- $\hat Q (s,a) \leftarrow r + \gamma max_{a'} \hat Q (s', a')$. Bellman Optimality Equation
- 현재 보상 + 미래 최적 보상

## TD error
- 현재 추정 : Q(s,a)
- 벨만 방정식 목표 : $r + \gamma max_{a'} Q(s',a')$
- 둘의 차이 = $\delta = r + \gamma max_{a'}Q(s',a')-Q(s,a)$
- 예상보다 어땠는지를 예측

## Q-Learning update
- $Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma max_{a'} Q(s',a')-Q(s,a)]$

