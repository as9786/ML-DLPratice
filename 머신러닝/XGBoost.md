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
- 
