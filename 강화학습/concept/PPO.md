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

$$
L^{CPI}(\theta)
=
\hat{\mathbb{E}}_t
\left[
\frac{\pi_{\theta}(a_t \mid s_t)}
{\pi_{\theta_{\mathrm{old}}}(a_t \mid s_t)}
\hat{A}_t
\right]
=
\hat{\mathbb{E}}_t
\left[
r_t(\theta)\hat{A}_t
$$ 
\right]
$$
