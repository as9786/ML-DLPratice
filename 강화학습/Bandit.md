# Multi-Armed bandit

- 여러 선택지 중 어떤 선택을 계속 해야 가장 큰 보상을 받을 수 있을까
- 팔이 여러 개 달린 slot machine
- Exploration vs Exploitation. 지금 좋은 걸 계속 쓸지 아니면 새로운 걸 시도할지
- Exploration : 다른 arm도 시도해보기
- Exploitation : 현재 가장 좋아보이는 arm 사용. Ex) B가 잘 되는거 같으니, B만 쓰자
- 강화학습보다 단순. 현재 선택만 존재
- 상태 전환이 없음. 미래 상태 없음. 행동 하나 선택 후 보상만 받음
- 각 arm의 기대 보상 : $\mu_a=E[R_a}$
- 가장 보상이 높은 arm 찾기
- Regret : 최적 arm을 안 골라서 손해본 양
- $Regret(T) : T_{\mu^*}-\sum_{t=1}^T r_t$
- 최적의 전략 대비 얼마나 손해를 봤는가
