# 차원 축소(Dimension reduction)
- Data preprocessing, visualization에서 중요
- 주성분분석은 주성분이 아닌 부분은 완전히 무시됨
- 차원 축소 시, 원래 차원에서의 주변 데이터와의 거리를 최대한 보전 -> SNE(Stochastic Neighbor Embedding)

# SNE

- 고차원(N)의 data(x) n개를 동일한 개수의 저차원(M)의 data(y)로 만들고자 함
- 차원을 줄이더라도 data 간 거리는 원래와 유사하게
- $$x_i(x_{i,1},x_{i,2},x_{i,3},\cdots, x_{i,N}) -> y_i(y_{i,1}, y_{i,2}, \cdots, y_{i,M})$$
- $$ 1 \leq i \leq n$$

## Data 간의 거리 및 선택 확률 분포
- 일반적인 거리는 euclidean distance
- $$D_{ij} = ||x_i - x_j||$$
- Data의 분산 정도에 따라 그 거리의 의미가 달라짐. 분산으로 위 값을 나누어 정규화
- $$_{ij}^2=\frac{||x_i-x_j||^2}{2 \sigma^2}$$
- 아래 2를 곱해주는 것은 나중에 활용할 표준 정규 확률 분포의 정의와 같게 하기 위함
- 위의 수식에서 분산은 모든 x들에 대해 구한 값
- 많은 data 중에서 $x_i$ 주변만 관심이 있다면, $x_i$ 주변의 특정 개수의 data만 가지고 분산을 구하는 것이 타당
- 위의 수식을 dissimilarities라고 부름
- 분산을 $x_i$ 주변의 이웃인 k개만 가지고 구함
- 해당 k를 perplexity라고 함
