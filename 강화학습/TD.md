- DP is a form of planning that builds strategies through evalutation using complete knowledge of the environment
- MC is a form of learning that learns through prediction using incomplete knowledge of the environment

# Temporal Difference Learning
- 환경에 대한 완전한 정보 없이도 진행이 가능한 학습의 한 종류

## Bootstraping
- Predictions about a population can be modeled by resampling sample data and performing predictions on the resampled samples
- 새 추정 <- 이전 추정 + 단계 크기 [목표 - 이전 추정]
- MCP(목표에 보상이 들어감) : $V(S_t) \leftarrow V(S_t) + \alpha [G_t - V(S_t)]$

- 목표에 가치 함수가 들어가게 되면 TP
- $V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]$
- 갱신의 목표점이 다음 상태에 대한 가치 함수 값. Utilizing prediction equations from previous episodes
- 실시간으로 값을 갱신할 수 있음
- 다음 상태에 대해 이전 가치평가를 기준으로 구하여 이를 갱신식의 목표로 삼아 현재 가치함수를 평가하고 새 정책을 구성
- MC operates with a long-term perspective, whereas the TD reflects changes in the estimate through step-by-step adaptive updates
- 학습 속도가 제한된 상황에서 효과가 뛰어남
- TD can operate even in episodes that may continue indefinitely
- Batch updating
- 갱신의 과정에서 각 시점에서의 예측마다 갱신하는 방식. 반복적으로 수행해 최종 결과에 도달
- 최대 가능도 추정

## 확실-등가 추정(Certainty-Equivalence Estimation)
- If a specific model B is derived for an unknown model A based on a bootstrapping estimation method, then model B is 
