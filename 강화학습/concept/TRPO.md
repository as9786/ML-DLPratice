# Trust Region Policy Optimization

## 초록
- 확률적 정책 기반의 정책 최적화 기법
- Trust region : 성능이 상승하는 방향으로의 최산화를 보장할 수 있는 구간. TRPO는 이 성능이 더 나은 정책으로 향하기 위한 최적화 기법에 대한 방법론
- 정책을 최신화할 때, 한 번에 너무 크게 바꾸지 않는 정책 최적화 기법
- 정책 최적화 : 정책 자체를 직접 최적화
- Monotonic imporvement : 최신화 시 성능이 이전보다 나빠지지 않도록 함

## 서론
- 정책 경사도 방법은 직접 정책을 학습할 수 있다는 장점
- 정책 최신화가 너무 크면 성능이 급격히 나빠질 수 있음
- DQN도 학습이 불안정하지만, 가치 기반 방법이고 replay buffer, target network 등을 통해 안정화
- TRPO는 정책을 얼마나 바꿔도 안전한지를 고려
- Surrogate objective, KL divergence constraint 사용
- Surrogate objective : 실제 정책 성능을 직접 최적화하기 어렵기 때문에, 현재 정책 주변에서 대신 최적화할 수 있는 근사 목적함수
- TRPO 기본 방향
1. 현재 정책으로 data 수집
2. 이 data를 이용해 새 정책이 좋아질 방향을 계산
3. 이전 정책과 새 정책이 너무 멀어지지 않도록 제한
- KL divergence : 두 정책의 멀어짐 정도를 측정하는 도구
- Large nonlinear policy : 신경망 정책에도 적용 가능

## 방법
- 좋은 방향으로 정책을 최신화하되, 이전 정책과 새 정책의 차이가 너무 커지지 않게 함

### 기본 정책 경사도
- 아래와 같은 목적을 최대화
- $J(\theta)=E[R]$
- 최신화 방법 : $\theta \leftarrow \theta + \alpha \nabla \theta J(\theta)$
- 학습율이 너무 크면 정책이 크게 망가질 수 있음
- TRPO : 성능은 좋아지는 방향으로 가되, 정책 변화량 제한

### Surrogate objective
- $L(\theta)=E[\pi_{\theta} (a|s) / \pi_{old}(a|s) * A_{old}(s,a)]$
- $\pi_{\theta} (a|s) / \pi_{old}(a|s)$ : 새 정책이 이전 정책에 비해 특정 행동의 확률을 얼마나 키웠는지
- A : Advantage. 이 상태에서 이 해동이 평균보다 얼마나 좋은가
- A(s,a) = Q(s,a)  V(s)
-  A > 0 : 좋은 행동이므로 확률을 높임
-  A < 0 : 나쁜 행동이므로 확룰을 낮춤

### Trust region constraint
- $D_{KL} (\pi_{old} || \pi_{\theta}) \leq \delta$
- 이전 정책과 새 정책의 KL divergence가 일정 값보다 작아야 함
- Maximize surrogate objective subject to KL(old policy, new policy) $\leq \delta$
- 제약이 있는 최적화 문제를 품

### 실제 최적화 (Conjugate gradient + Line search)
- 위 제한된 최적화는 그대로 풀기 어려움
- 정책이 신경망이면 가중치의 수가 매우 많음
- 아래와 같은 근사 사용
1. Surrogate objective 1차 근사
2. KL constraint 2차 근사
3. Conjugate gradient로 최산화 방향 계산
4. Line search로 실제 step size 조정

### Conjugate gradient
- Ax=b
- A가 너무 크면 역행렬을 구하기 어려움
1. 일단 아무 값으로 시작
2. 현재 오차의 잔차를 계산
3. 오차를 줄이는 방향으로 이동
4. 이전 방향과 겹치지 않는 새 방향을 만듦
5. 반복

### Line search
- 특정 방향으로 얼마나 크게 이동할 것인가
- Backtracking line search : 큰 step size로 시도 후 점차 줄여나가 안전한 지점을 찾음

