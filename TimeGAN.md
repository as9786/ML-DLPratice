# Time-series Generative Adversarial Networks

## Abstract & Introduction

- 기존의 시계열 생성 모형
1. GAN-based
2. Seq2Seq

- GAN 기반 생성 모형은 cv에서 처음 등장했기 때문에 시간적인 정보를 사용 X
- 영상은 공간적 정보가 있지만 그 관계를 순환신경망과 같이 시간적 정보를 사용 X
- Seq2Seq 기반 모형은 지도 학습이기 때문에 deterministic(결정론적 : 예측한 그대로 동작)
- Train data 이외의 data는 생성하기 힘듦
- GAN = 비지도 = 비-결정론적 = open-loop
- Temporal correlations = 지도 = inherently deterministic = closed-loop
- 해당 논문은 비지도와 지도 학습을 동시에 진행하는 생산적 적대 모형 제시
- 비지도는 학습이 어려운 대신 새로운 train data distribution을 제공하고, 지도 학습 부분은 학습이 쉬운 대신 뻔한 data 생성
- 위의 두 가지 장점을 결합
- 해당 논문의 공헌도
1. 비지도 손실과 지도 손실을 동시에 사용
2. Embedding network를 통하여 생성기가 train data의 잠재 표현을 생성하는 방식 제시
3. Time-series에는 거의 변하지 않는 정적인 특징(나이, 이름)과 시간마다 변하는 일시적 특징을 구분하여 훈련

## Method

### Closed-loop
- 자기 회귀 모형처럼 이전의 정보들의 선형 조합으로 새로운 것을 생성하는 것은 기존의 data와 크게 다르지 않은 것을 생성
- Markov chain

### Open-loop
- Closed-loop와 달리 조건이 없음. Train data distribution을 한 번에 생성
- Data를 한 번에 얻을 수 있음. Train data에 국한되지 않는 data를 생성 가능
- 시간적인 상관 관계 고려 X

### Problem Fomulation

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/e9522c76-ca0f-4289-a599-5316188edb0c)

- 비지도 손실과 지도 손실을 둘 다 학습하기 때문에 손실 함수를 크게 2가지로 표현
- 비지도 손실
![image](https://github.com/as9786/ML-DLPratice/assets/80622859/1853caba-b7f0-4271-9b96-30ace9e00c3d)

- D는 두 확률 분포를 나타내는 함수. D가 JS divergence라면 GAN loss와 같음
- 지도 손실

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/6220e3ad-799b-44c4-9286-5de9069f8a9f)

- 비지도 손실에서 과거 변수들이 조건으로 들어가 있음

### Model Architecture
- 크게 4가지로 구성
1. Embedding layer
2. Recovery layer
3. Generator
4. Discriminator(s와 x 존재. 정적인 특징과 일시적 정보를 두 개 다뤄야하기 때문)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/ad155385-0aa0-421a-b381-d8ee24494c72)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/ffb9038a-47ce-45b2-8dd1-5a89c0679418)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/06793cb2-dd55-47c1-bd41-4deeaf3958cc)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/992c7771-e5a9-442e-89dc-14cf90c174c8)

- 총 5가지로 학습
1. Auto encoder
2. Supervisor
3. Generator
4. Autoencoder
5. Discriminator
