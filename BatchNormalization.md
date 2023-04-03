# Batch Normalization

## 일반 경사 하강법(Vanilla Gradient Descent)

- 경사를 한 번 update를 하기 위해 모든 학습 data를 사용

## 확률적 경사 하강법(Stochastic Gradient Descent)

- SGD
- 경사를 한 번 update 하기 위해 일부의 data만을 사용(Batch size개의 경사 평균)

## Mini-batch

- 학습 data 전체를 한 번 학습하는 것을 epoch
- 한 번 경사를 구하는 단위 batch
- Epoch마다 data 순서를 섞어 주기도 함

## Internal Covariate Shift

![image](https://user-images.githubusercontent.com/80622859/221401815-f96bc7ad-2a77-4897-9718-8b4216bc7f04.png)

- 학습 과정에서 계층별로 입력의 data 분포가 달라지는 현상 
- 이를 해결하기 위해 batch normalization

## Batch Normalization

![image](https://user-images.githubusercontent.com/80622859/221401911-70bbf451-7072-46ff-88e9-167eab46c435.png)

- 학습 과정에서 각 batch별로 평균과 분산을 이용해 정규화하는 계층

### 학습 단계(Training phase)

![image](https://user-images.githubusercontent.com/80622859/221401972-a9179d51-ffa2-4f8b-83a3-7c9efec4b14f.png)

- Batch 별로 계산

![image](https://user-images.githubusercontent.com/80622859/221402066-a5a66c49-096b-4b16-9e8d-f69f8339a767.png)

- 정규화로 인해, 모든 계층의 feature가 동일한 scale이 되어 학습률 결정에 유리
- 추가적인 scale, bias를 학습하여 활성화함수에 적합한 분포로 변환
- ReLu를 적용하게 되면 0 이하의 값들이 전부 0으로 되어버리기 때문에 $\gamma, \beta$ 를 적용
- $\gamma$ : scaling factor, $\beta$ : 편향

### 추론 단계(Inference phase)

![image](https://user-images.githubusercontent.com/80622859/221402104-6d19fb92-cea1-402c-97fc-daff5d7aff05.png)


- 추론 과정에서는 학습 과정에서 평균과 분산을 이동 평균(지수 평균)하여 고정
- 이동 평균에서는 최근 N개만 사용을 하기 때문에 지수 평균을 사용하는 경우도 있음 
- 추론 단계에서는 정규화와 추가 scale, bias를 결합하여 단일 곱, 더하기 연산으로 줄임

## 전결합 계층과 결합

![image](https://user-images.githubusercontent.com/80622859/229456127-d6a2ed2d-1c8f-40df-8891-b27f90d7c075.png)

- 전결합 계층의 편향이 batch norm의 편향과 역할이 겹치므로, 전결합 계층의 편향을 제거

## 합성곱 계층의 batch normalization

![image](https://user-images.githubusercontent.com/80622859/229456776-0b4178cf-616d-43db-a2db-1a3ed85edf70.png)

- 전결합 계층은 각 node 별로 정규화
- 합성곱 계층은 각 channel 별로 정규화
- 배치, 높이, 너비에 대해 평균과 분산을 계산

## 한계

- Mini-batch에 의해 크게 영향을 받음
- Batch의 크기가 너무 작으면 잘 작동하지 않음 => Sample 자체가 평균이 되어 버림
- Memory의 한계로 RNN이나 크기가 큰 CNN에 적용하기 어려움
- Batch의 크기가 너무 커도 잘 동작 X(Gaussian Mixture)
- 병렬화 연산 효율이 떨어짐, 학습 속도 증가



