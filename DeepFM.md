# DeepFM: A Factorization-Machine based Neural Network for CTR Prediction

- Click-through rate prediction

## Abstract

- CTR을 예측하는 모형
- FM과 DL을 통합, 특징들의 상호 작용을 모형화
- 기존 모형들은 low-order feature interaction 또는 high-order feature interaction 중 하나만 고려
- DeepFM은 두 상호작용을 모두 표현
- Wide & Deep model과 달리 FM part와 DL part가 같은 입력을 공유 => 별도의 feature engineering이 필요 없음

## Introduction

### Goal

- CTR prediction은 사용자에게 추천 제품이 주어졌을 때, 사용자가 해당 제품을 click할 확률을 추정
- 추정된 확률을 바탕으로 사용자의 선호 제품 순위를 메길 수 있음

### Feature interaction

- Ex) 사람들은 식사시간에 배달앱을 다운로드하는 경향이 있다. -> 앱과 시간 간의 상호작용(order-2)
- Ex) 10대 남자들은 RPG game을 선호 -> game, 성별, 나이 간의 상호작용(order-3)
- Ex) 사람들은 맥주와 기저귀를 함께 구매하는 경향이 있다. -> 맥주와 기저귀 간의 숨겨진 상호작용 
- 명시적인 상호작용과 숨겨진 상호작용을 잡아낼 수 있는 모형이 중요 => DeepFM은 두 part로 구성

### Previous studies

- Generalized Linear Model(GLM) : 일반적으로 order-2 interaction까지만 고려. 그 이상은 일반화 어려움
- Factorization Machine(FM) : low-order 뿐만 아니라 high-order interaction도 모형화 가능 => 복잡도가 커짐
- Factorization Machine supported Neural Network(FNN) : High-order interaction까지 모형화 가능. Low-order를 포착하기 어려움
- Wide & Deep : 선형 모형과 신경망 모형을 통합. 전체적인 상호작용을 포착 가능. Wide의 경우 고도의 feature engineering 필요

### Contribution

- DeepFM은 모든 상호작용 포착 가능
- End-to-end, 별도의 feature engineering 필요 X

![image](https://user-images.githubusercontent.com/80622859/227768203-b5efe322-31fa-41fc-a224-8187a46ba373.png)

- FM과 DL이 입력과 embedding vector를 공유

## Our Approach

![image](https://user-images.githubusercontent.com/80622859/227768220-134d5a98-cd39-4f4b-9f0d-19ec2dfbafa4.png)

- n개의 data
- 각 행은 사용자와 제품 정보를 담고 있음(x), click 여부(y)
- User field에는 사용자의 id, 성별, 나이 등의 정보, item field에는 특정 제품의 구매 정보 등
- 명목 변수일 경우에는 one-hot vector, 연속 변수일 경우에는 해당 값을 그대로 사용
- x는 매우 sparse하며 고차원
- y = 0 or 1

![image](https://user-images.githubusercontent.com/80622859/227768362-efe13669-f7d7-41e5-b8fb-bb527a26229d.png)

## Deep FM

![image](https://user-images.githubusercontent.com/80622859/227771707-6183f223-34a4-4184-8c5d-7c3e59581a11.png)

- low-order feature interaction -> FM
- High-order feature interaction -> DL

### Input

- FM and DL have the same embedding vector
- Difference from Wide & Deep
- 별도의 embedding layer를 훈련시켜 얻은 dense vector

![image](https://user-images.githubusercontent.com/80622859/227771768-d3b23460-6955-4e1b-9846-11d429e0077c.png)

- 각 신경망은 hidden vector의 차원이 k로 모두 동일
- 이러한 훈련 과정에서 얻은 가중치 행렬의 각 행이 각 x의 embedding vector
- Word2Vec과 유사
- Ex) 연령이 [10대, 20대, 30대]

