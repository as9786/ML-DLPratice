# XGBoost : A Scalable Tree Boosting

- 확장성이 우수

## 1. Introduction
- Out-of core(탈중앙화) 계산 방식으로 빠름
- Hardware와 algorithm 모두에서 장점

## 2. Tree Boosting In a Nutshell

### 2.1 Regularized Learning Objective

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/58e6e771-2505-4ff9-bace-5e2b715d3164)

- 각각의 tree는 입력을 받아 출력으로 어떠한 값을 내고, 각각의 tree로부터 받은 값들을 합친 것을 최종 예측 값으로 결정
- n x m(n : samples, m : features) Dataset $D = {(x_i,y_i)}, (|D| = n, x_i \in R^m, y_i \in R)$에 대하여, Tree ensemble model은 K개의 tree를 사용

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/52dfde1b-d0bc-4f0e-a39b-8f143cfdb97a)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/3b3393cf-741c-4329-bceb-1c13e4a8a25b)

- F는 regression tree를 나타냄
- T : Tree의 leaf 수
- XGBoost는 위의 tree를 학습하는데 정규화된 손실 함수(regularized loss function)를 사용

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/13feeae4-83b9-476c-8588-d67023e4fc98)

- L : 손실 함수
- l : 실제 출력값과 예측값 사이의 차이를 계산하는 미분 가능한 아래로 볼록한(convex) 손실 함수
- $\Omega$ : 각 tree에 대한 regularization term. 직관적으로 T가 작고(모형이 단순), L2 norm이 작은 모형의 과적합을 방지
- 전통적인 gradient tree boosting 방식에서는 정규화 부분이 없음
- 위의 식에서 $\gamma, \lambda$가 0이면 기본 gradient tree boosting과 같음

### 2.2 Gradient Tree Boosting

- 어떤 data로부터 분류 기능을 가장 잘 수행하는 tree를 찾는 문제는 NP-완전 문제. 가능한 모든 tree로부터 가장 좋은 tree를 찾는 것은 어려움
- 가장 좋은 tree를 찾기 위해서, 매 반복마다 tree에 가지(branch)를 하나씩 늘려나가는 방식(additive manner)을 제안

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/0dda60a1-875e-4d44-b477-811d4e8a623e)

- $L^t$ : t 번째 반복에서 계산할 손실 함수
- l : 임의의 손실 함수, $y_i$ : i번째 표본의 실제 값, $\hat y^{t-1)$ : t-1 번 째에서 나온 예측 값
- $f_t(x_i)$ : t번 째 반복에서의 tree에 i번 째 data를 넣은 예측 값
- 마지막 Constant는 t-1번 째까지의 정규화 부분의 합(상수)
- 위의 식이 왜 XGBoost가 GBM 모형인지를 알려줌
- GBM은 ensemble 진행하는 과정에서 이전 iteration에서 잘 학습하지 못한 부분에 가중치를 두고 학습하는 방식
- 위의 식을 손실 함수 하에서 최적화하기 좋은 형태로 만들기 위해 Taylor expansion을 통한 2차 근사(second-order approximation)
- 
