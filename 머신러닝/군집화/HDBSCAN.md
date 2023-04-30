# HDBSCAN

## 1. Transform the space according to the density/sparsity
- 거리를 robust하게 만듦
- 계층적 군집화는 작은 거리에도 민감하게 반응. Noise로 생긴 거리로 인해 계층이 심하게 변동
- Transformed distance metric

![image](https://user-images.githubusercontent.com/80622859/235342223-ca6c12a2-2649-47be-8323-6aa6eb4a7d3c.png)

- $core_k(a)$ : a의 k-th nearest neighbor까지의 거리
- Mutual reachability
- 두 점 a와 b의 거리를 잴 때
1. a의 이웃과의 거리
2. b의 이웃과의 거리
3. a와 b 자체의 거리
- 1,2,3 중 최대값을 고름
- 밀도가 높은 지점은 core의 거리가 매우 작기에 d(a,b) 사용,  밀도가 낮은 지점의 경우에는 우연히 한 점이 바로 옆에 존재해도 core의 정보 사용
- 거리의 robustness를 늘리고, 최종적으로 더 효율적인 군집화 가능
- Noise point에 의해서 서로 멀리 떨어진 군집이 하나로 묶이는 것을 방지

## 2. Build the minimum spanning tree of the distance weighted graph

- Mutual reachability를 이용하여 각 data들 간의 거리를 구함
- 이를 이용해서 graph 생성
- Data : 꼭짓점, edge : 점수(mutual reachalbility)를 부여
- 거리가 가중치인 graph. 길이가 길수록 가중치가 커짐
- 가중치보단 점수 또는 식별자로 이해하면 됨
- Tree의 적합은 아직 추가되지 않은 점 중 가장 가까운 edge를 하나씩만 추가하며, 결과적으로 모든 점을 포괄할 때까지 tree를 키워나감

![image](https://user-images.githubusercontent.com/80622859/235342693-a786e97b-7d3e-43cd-9911-dc5954a44b83.png)

