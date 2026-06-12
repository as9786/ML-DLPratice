# Proximal policy optimization algorithms

## 초록
- First-Order optimization만을 사용해 구현이 쉬움
- TRPO만큼의 성능을 지님. Data efficiency 문제 해결

## 1. 사전 연구
- Trust region methods : 특정 제한 내에서 목적 함수가 최대화 되는 정책 최신화 진행

## 2. 방법

### 2-1. Clipped surrogate objective
- 확률 비율 : $r_t(\theta) = \frac{\pi_{\theta} (a_t|s_t)}{\pi_{\theta_{old}} (a_t|s_t)}$
- 기존의 surrogate objective 함수에 적용

$$L^{CPI}(\theta)=\hat{\mathbb{E}}_t\left[\frac{\pi_{\theta}(a_t \mid s_t)}{\pi_{\theta_{\mathrm{old}}}(a_t \mid s_t)}\hat{A}_t\right]=\hat{\mathbb{E}}_t\left[r_t(\theta)\hat{A}_t\right]$$

- CPI : Conservation Policy Iteration
- 위 목적을 최대화하게 되면 정책 최신화가 큰 단계로 진행될 가능성이 있음
- 천천한 향상을 보장할 수 없음
- 기존 정책과 많이 다른 정책에 penalty 부과
- 새로운 목적 함수 제안

$$L^{CLIP}(\theta)=\hat{E}_t[min(r_t(\theta)\hat A_t, \ clip(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat A_t)]$$

- $\eta$ : 초매개변수, 기본값=0.2
- 첫번째 항은 기존 목표. 두번째 항은 clipped probability ratio 적용
- 위 두 개를 비교해 더 작은 값을 취함으로써 lower bound 형성

### 2-2. Proximal policy optimization
- 미분 가능하도록 수정
- Policy surrogate + Value function error

$$L_t^{\mathrm{CLIP+VF+S}}(\theta)=\hat{E}_t\left[L_t^{\mathrm{CLIP}}(\theta)-c_1L_t^{\mathrm{VF}}(\theta)+c_2S(\pi_\theta)(s_t)\right]$$

- C : 각각 손실함의 비중을 결정하는 계수. $L_{VF}$ : 가치 함수의 제곱 잔차 손실, S : Entropy bonus
- T만큼의 길이만큼 trajectory segment를 하나의 미니 배치로 사용
- 매 반복마다 N개의 행동이 t만큼 data를 모아 최신화하는 방식
- SGD를 통해 최신화 
