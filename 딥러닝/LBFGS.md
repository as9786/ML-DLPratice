# Limited-memory quasi-Newton methods 

## 소개
- Hessian matrix를 계산하거나 저장하기 위한 비용이 합리적이지 않을 경우 사용
- n x n의 hessian matrix를 저장하는 대신 n차원의 vector 몇 개만을 유지하여 Hessian matrix를 추정하는 방식
- BGFS를 기반으로 함
- 가장 최근의 반복들에서의 curvature information을 이용

## BFGS 
- quasi-Newton algorithm. Computer memory의 제한된 양만을 사용
- 사람 이름의 앞 글자들만 합쳐 놓은 것 

<img width="1107" height="53" alt="image" src="https://github.com/user-attachments/assets/58aad888-6354-41af-9dee-8ef0ba01e6bc" />

- BFGS 목적은 f(x)를 제한 조건이 없는 실수 vector x에 대해서 최소화 시키는 것.(f(x)는 scalar function)
- Scalar function : 결과 또는 출력이 단일 값인 함수
- 이차 도함수를 직접 계산하지 않고, 매 반복마다 근사해서 parameter를 최신화하는 방법

### 과정
1. 현재 위치 $x_k$에서의 경사 계싼 : $g_k=\bigtriangledownf(x_k)$
2. 
