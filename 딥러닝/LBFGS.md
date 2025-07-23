# Limited-memory quasi-Newton methods 

## 소개
- Hessian matrix를 계산하거나 저장하기 위한 비용이 합리적이지 않을 경우 사용
- n x n의 hessian matrix를 저장하는 대신 n차원의 vector 몇 개만을 유지하여 Hessian matrix를 추정하는 방식
- BGFS를 기반으로 함
- 가장 최근의 반복들에서의 curvature information을 이용

## BFGS 

<img width="1107" height="53" alt="image" src="https://github.com/user-attachments/assets/58aad888-6354-41af-9dee-8ef0ba01e6bc" />


