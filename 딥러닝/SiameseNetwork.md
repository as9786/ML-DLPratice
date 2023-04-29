# Siamese Neural Networks

- 샴 쌍둥이에서 착안된 신경망
- 두 신경망의 구조가 서로 닮아있으며, 더 나아가 가중치를 공유

# Siamese Neural Networks for One-shot Image Recognition
- One-shor learning 분야

## One-shot learning

- DL model을 학습시키기 위해서는 많은 양의 data가 필요
- 모든 data에 대해 labeling을 해야 함
- 사람은 적은 data로도 학습이 가능
- DL model이 사람처럼 소량의 data만으로도 학습을 할 수 있는 것을 few-shot learning이라고 함
- One-shot learning은 few-shor learning의 극단적인 예시로, 한 장의 data만으로도 학습을 할 수 있는 것

## 학습

- 두 사진을 입력으로 받고, 동일한 CNN으로 두 사진에서 visual embedding을 각각 추출
- 해당 visual embedding 간의 거리를 구하고 거리를 유사도 값으로 출력(0~1)

![image](https://user-images.githubusercontent.com/80622859/235295035-09c14a41-3b40-4a90-ba1a-e895f75a565b.png)

1. 입력값 두 개 준비. 동일한 class일 경우 출력값을 1, 다를 경우 0으로
2. 가중치를 공유하는 합성곱 신경망을 통과시켜 각 입력에 대한 embeddings 얻음
3. 두 embeddings 거리 계산(L1 norm, L2 norm)
4. 입력이 같은 class면 거리를 가깝게, 다른 class면 거리를 멀게 하는 contrastive loss를 이용하여 학습


# Constrastive loss

- 규원이가 남선, 성주, 동호의 사진을 각각 100 개 씩 가지고 있다고 가정
- 무작위로 2장의 사진을 뽑아 짝을 지어서 image set을 구성
- 같은 사람일 경우 1, 다른 사람일 경우 0
- {(남선-남선,1),(성주-남선,0),(남선-동호,0),(성주-성주,1)}
- 각각의 사진에서 합성곱 신경망을 이용하여 embedding을 추출하고 거리를 이용하여 손실 계산

- $Loss(i,j) = y_{ij}D^2_{ij} + (1-y_{ij}) \times max(0,\alpha - D^2_{ij})$
- Label = 1인 경우 embedding 간의 거리가 손실이 됨($y_{ij} = 1$)
- Label = 0($y_{ij}=0$)인 경우에는 아래와 같이 식이 작성 됨
- $max(0,\alpha - D^2_{ij})$  
- $\alpha > D^2_{ij}$인 경우 $loss = \alpha-D^2_{ij}$ => 가중치 최신화
- $\alpha \leq D^2_{ij}$인 경우 $loss = 0$ => update X
