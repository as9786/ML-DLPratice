# 1. Model-Free
- Model-based methods have the drawback of high computational cost
- When the enviroment's MDP is unknown, reinforcement learning enables an agent to learn through trial and error by interacting with the environment
- Sample backup
- Prediction estimates the value function of the current policy through sample backups and control updates the policy using the estimated value function

# 2. Monte-Carlo Approximation
- Estimate the target value using random sampling

# 3. Monte-Carlo prediction
- 현재 정책의 가치 함수를 실제 경험(sampled episode)을 통해 추정하는 방법
- 직접 여러 번 행동해보고, 실제로 얻은 보상의 평균으로 상태의 가치를 추정
- 환경 모형이 필요 없음
- $V^{\pi} (s)$
- 현재 정책을 따라 행동했을 때, 상태가 얼마나 좋은 상태인가?
- 실제 episode를 끝까지 진행한 뒤 보상을 계산
- $G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots$
- 현재 시점 이후 미래 보상들의 할인율이 적용된 합

## 3-1. 최신화 방법
- $V(s) \leftarrow V(s) + \alpha (G_t - V(s))$

