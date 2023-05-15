# Local Outlier Factor

- 기존의 방법들은 지역 정보에 대한 고려 X
- Data들 간의 특성에 따라, 어떤 집단에서는 매우 가까운 거리가 어떤 집단에서는 매우 먼 거리일 수도 있음

- Density based method는 density가 상이한 군집들이 있을 때 문제 발생
- 기존의 densed based 방법론들은 dense라는 개념을 정의하기 위해 특정한 window size나 최소 갯수 등을 이용
- Ex) dense : 거리가 c이하인 window 내에 들어오는 data가 k개 이상인 경우
- Density가 상이한 경우, 기존의 방법론처럼 절대적인 기준을 지정 불가

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/cdd3f8af-26ed-4d10-9c82-54ecb9a474e0)

- C1과 C2의 density가 다르기에, o1은 쉽게 확인 가능
- 하지만 o2는 이상치로 탐지하기 어려움
- C1의 대부분의 점들이 C2 집단 내에서 o2까지의 거리와 비슷하기 때문
- 일정 거리를 기준으로 삼게 되면, C1 또는 C2에만 특화된 이상치 탐지를 사용하게 됨
- 위와 같은 문제에서 지역의 상대적인 밀집도를 비교하여 이상치를 탐지하는 방식이 LOF
- 이웃들의 밀집도를 고려하여서 비교

## 1. k_distance(p)

- 특정 data p에서 k개의 근처 이웃까지의 거리
- 3_distance(p) : 3 번째로 가까운 data와의 거리
- 거리가 1,2,3,3,3 과 같이 겹치는 경우에는 k_distance 내에 1개 이상의 이웃이 존재할 수 있음
- $N_k(p)$ : k_distance(p) 안에 들어온 data의 개수

## 2. Reachability distance(p,o)

- reach_dist(p,o)
- p에 대해서 생각할 때, 주변 data o의 k_distance를 고려한 거리
- reach_distance(p,o) = max(k_distance(o), dist(p,o))
- p와 o가 매우 붙어있더라도, o의 k_distance만큼은 거리를 유지하겠다는 개념
- 너무 작은 값을 같지 않도록 해줌
- 
