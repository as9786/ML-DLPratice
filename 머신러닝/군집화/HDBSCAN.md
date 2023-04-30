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

## 3. Construct a cluster hierarchy of connected components
- 점수를 낮추면서 하나씩 graph를 끊음. 0.9인 지점의 연결선을 끊고, 0.8인 연결선을 끊고...
- 그 후, 만들어진 minimum spanning tree를 가장 가까운 거리부터 hierarchy clustering처럼 묶음
- 가장 가까운 점 하나만 있으면 그것을 연결(Single linkage). 단순 거리가 아닌 mutual reachability를 사용했으므로 robust single linkage라고 함

![image](https://user-images.githubusercontent.com/80622859/235342784-7a553e80-8c3c-41a6-b83f-57670d36d3c5.png)

## 4. Condense the cluster hierarchy based on minimum cluster size
- Threshold distane가 내려가면서 계층이 분할될 때, data가 1개, 2개 떨어져 나오는 경우 발생. 지저분 해짐
- 위의 그림 기준으로는 거리가 0.4 이하로는 거의 다 data가 한 개가 떨어져 나옴
- 이런 경우에는 2개의 군집이 나눠진 것으로 보지 않고, 한 개의 군집이 data를 잃은 것(fell out)이라고 정의
- Noise로 처리
- Minimum size(초매개변수) 지정
- 최종적으로는 minimum size 이상의 크기를 가진 군집들이 남게 됨

![image](https://user-images.githubusercontent.com/80622859/235342916-6af75535-c1bc-4dd7-89fd-7c1be44f919e.png)

## 5. Extract the stable clusters from the condensed tree 

- 위의 과정들은 단순히 noise를 제거. Local density 반영 X
- Minimum size를 만족하기는 했지만, 마지막에 분할된 군집들이 존재
- 이상적인 군집은 위의 그림에서 오랫동안 지속되었던 군집들
- 이와 같은 직관을 수식으로 정의 -> HDBSCAN
- 새로운 군집이 생기고(birth), 그 중 noise로 fell out 되는 data가 몇 개씩 존재하다가, 결국에는 minimum size 이상의 2개의 군집으로 분할(death)
- 마지막에 분할이 안 되고 계속 지속되는 군집 존재. Noise로 fell out 되는 점들은 거리를 만족하지 못하고, minimum size를 만족하지 못하는 애들
- 우리가 찾고 싶은 군집은 오래 살은 군집
- $\lambda_{birth}$ : 군집의 탄생된 값, $\lambda_{death}$ : 한 군집이 두 개의 군집으로 분할되는 시점
- 해당 군집 내의 각 점들은 fell out 되었다면 해당 시점이 존재하는 해당 시점을 $\lambda_p$로 표현
- 끝까지 남아 있는 점들은 $\lambda_p = \lambda_{death}$
- 군집 안정성(Cluster stability)

![image](https://user-images.githubusercontent.com/80622859/235343120-6e2c21f0-8358-4f03-a6b6-1ea1b3211817.png)

1. 이를 각각의 점에 대해서 모두 실행(부모, 자식 가릴 것 없이 아래에서 위로 올라가며 모두 실행)
2. 아래에서 위로 올라가며 두 개의 자식 군집이 부모로 합쳐질 때마다, 그 부모의 안정성과 두 자식 군집의 안정성의 합을 비교
3. 자식 군집의 안정성 합이 더 크면 2개의 자식을 군집으로 유지, 아닐 경우 부모를 군집으로 유지

![image](https://user-images.githubusercontent.com/80622859/235343214-f0c9a53a-1439-424e-96c1-eb103f4586ae.png)

### 결과물 및 각 data의 확률

- $\lambda_p$, 군집에서 떨어져 나간 시점들을 모아, 각 군집 내에서 [0,1]에 오도록 scaling
- 이 값이 큰 점들은 군집이 태어나자마자 fell out 된 애들이므로, 이를 해당 군집에 속할 확률으로 해석


