# HiPPO: Recurrent Memory with Optimal Polynomial Projections



## 방법

### High-order Polynomial Projection Operators

- 시계열 함수 f(t)를 정의
- f(t)에 사상(mapping)되는 공간(space)은 매우 큼
- 모든 시간(time, history)에 대해서 기억할 수 없음
- 적절한 부분공간(subspace)에 f(t)를 근사하여 문제 해결

### General HiPPO Framework

![image](https://github.com/user-attachments/assets/7b0a6014-c47a-4d09-a9f4-98353304d660)

1. 시간에 따라 변하는 함수 f를 정의
2. 각 시간($t_0, t_1...T$)에 따라 최적으로 투영되는 다항 함수 g(t)가 존재
3. 2의 g에서 각 (2+3을 합쳐서 HiPPO라고 함)
4. 시간변화율에 따른 continous-time HiPPO ODE(Ordinary Dynamic Equation) 정의(HiPPO ODE에서 f는 t 시점까지의 f 함수)
5. 현재 공간은 이산적이므로, 이를 회귀 문제로 재정의. 

- 시간 함수 f(t)를 투영(projection)시키고, 계수 행렬(coeff)로 사상해서 c(t)를 찾는게 HiPPO framework

### High Order Projection: Measure Families and HiPPO ODEs

1. translated Legendre(LegT)

2. 
