# 차원 축소(Dimension reduction)
- Data preprocessing, visualization에서 중요
- 주성분분석은 주성분이 아닌 부분은 완전히 무시됨
- 차원 축소 시, 원래 차원에서의 주변 데이터와의 거리를 최대한 보전 -> SNE(Stochastic Neighbor Embedding)

# SNE

- 고차원(N)의 data(x) n개를 동일한 개수의 저차원(M)의 data(y)로 만들고자 함
- 차원을 줄이더라도 data 간 거리는 원래와 유사하게
- $$x_i(x_{i,1},x_{i,2},x_{i,3},\cdots, x_{i,N}) -> y_i(y_{i,1}, y_{i,2}, \cdots, y_{i,M})$$
- $$1 \leq i \leq n$$

## Data 간의 거리 및 선택 확률 분포
- 일반적인 거리는 euclidean distance
- $$D_{ij} = ||x_i - x_j||$$
- Data의 분산 정도에 따라 그 거리의 의미가 달라짐. 분산으로 위 값을 나누어 정규화
- $$d_{ij}^2=\frac{||x_i-x_j||^2}{2 \sigma^2}$$
- 아래 2를 곱해주는 것은 나중에 활용할 표준 정규 확률 분포의 정의와 같게 하기 위함
- 위의 수식에서 분산은 모든 x들에 대해 구한 값
- 많은 data 중에서 $x_i$ 주변만 관심이 있다면, $x_i$ 주변의 특정 개수의 data만 가지고 분산을 구하는 것이 타당
- 위의 수식을 dissimilarities라고 부름
- 분산을 $x_i$ 주변의 이웃인 k개만 가지고 구함
- 해당 k를 perplexity라고 함
- k개만을 통해 분산을 구하게 되면 위의 i와 j의 순서가 바뀌면 다른 값이 됨
- 정규분포를 활용하면 $x_i$와 $x_j$의 거리를 확률로 나타낼 수 있고, $x_i$의 이웃 중에서 $x_j$를 선택할 확률은 다음과 같음
- $$p_i = \frac{e^{-d_{i,j}^2}}{\sum_{k \neq i} e^{-d_{i,k}^2}}$$

## 고차원 확률분포와 저차원 확률 분포 차이
- 고차원 data 사이의 선택 확률은 위의 수식으로 정의. 저차원 data $y_i$ 사이의 선택 확률도 동일하게 정의 가능
- 편의상 분산을 1/2로 가정(고차원에서 저차원을 구하려고 하는 것이기 때문)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/fb43b8f0-54c1-4872-8f1c-cb22c8e14a10)

- 위에서 정의한 확률 분포들이 가장 유사하게 $y_i$를 찾는 것이 목표
- 확률분포 사이의 차이를 나타내는 KLD 사용
- 임의의 $x_i$에 대한 비용 함수를 아래와 같이 정의

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/b7fbf944-2f3c-419e-b8e0-8c2ad66627bf)

- 모든 $x_i$에 대한 비용 함수는 아래와 같음

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/845079eb-a342-43cf-9c61-865062fc2749)

- 비용 함수를 최소화하는 $y_i$를 찾는 것

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/942f2ff3-bb26-47db-8758-1fdc7e226235)

- 정규분포 대신에t 분포를 활용하는 것이 t-SNE



