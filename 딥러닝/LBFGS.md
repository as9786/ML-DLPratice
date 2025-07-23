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
1. 현재 위치 $x_k$에서의 경사 계싼 : $g_k=\bigtriangledown f(x_k)$
2. 이전 단계 정보 계산
   - $s_k=x_{k+1}-x_k$
   - $y_k=g_{k+1}-g_k$
3. Hessian의 역행렬 근사치 $H_k$ 최신화

<img width="283" height="64" alt="image" src="https://github.com/user-attachments/assets/6a624168-aebe-45ea-93de-d09e279cfd83" />

4. 다음 위치 계산 : $x_{k+1}=x_k-\alpha_k H_k g_k$

## LBFGS 과정
- 목적 함수와 경사만 있으면 됨
- 선형 방정식을 풀지 않고 최적화 방향을 결정

### 수식 구조
- $x_{k+1}=x_k - \alpha \dot H_k \triangledown f(x_k)$
- $H_k$는 저장된 m개의 vector로 구성
- 고차원 최적화 문제에서 memery efficient
- SGD보다 더 정확한 최적화 뱡향이 필요할 때 사용

### Code

```{python}
from torch import optim

optimizer = torch.optim.LBFGS(model.parameters())
.
.
.
optimizer.step(loss)
``` 

