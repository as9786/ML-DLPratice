# Bellman equation
- 강화학습의 목표는 지금 행동했을 때 미래까지 포함해서 얼마나 좋은가를 계산
- 가치를 평가. V(s)=지금 받는 보상 + 미래 상태의 가치
- $V(s) = E[r + \gammaV(s')]$
- V(s) : 현재 상태 가치, r : 현재 보상, s' : 다음 상태, $\gamma$ : 할인율
- 할인율은 미래 보상을 얼마나 중요하게 볼지 결정. $0 \leq \gamma \leq 1$
- 할인율이 낮을수록 현재만 중요
- 미래 보상을 게속 더하면 발산하기 때문에, 할인율을 적용하여 안정화
- 예시
  - Ex) 상태 : 몬스터 앞, 행동 : 공격, 보상 : +10
  - V(s)=10 + 0.9V(s')
- 재귀 구조

# Bellman optimality equation
- $V^{*} (s) = max_a E[r + \gamma V^* (s')]$
- $max_a$ : 가능한 행동 중 가장 좋은 행동 선택
- 실제로는 상태만 보는 것이 아닌 상태 + 행동의 가치를 사용(Q-Function, Q(s,a))
## Bellman equation for Q
- $Q(s,a)=E[r+ \gamma max_{a'} Q(s',a')]$
- DQN, Q-learning의 수식 
