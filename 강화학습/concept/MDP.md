# Markov Decision Process
- Modeling the decision-making process using probabilities and graph structures. 시간 t에서의 상태는 t-1에서의 상태에만 영향을 받음(First-Order Markov assumption)
- $p(s_t|s_0,s_1,...,s_{t-1})=p(s_t|s_{t-1})$

## 1. Markov reward process
- Extending the Markov process by adding rewards to each state
- $<S, P,R, \gamma>$
- S : 상태의 집합. 미로 탈출 문제에서 현재 위치
- P : 각 요소가 $p(s'|s)=Pr(S_{t+1}=s'|S_t=s)$인 집합. p(s'|s)는 현재 상태 s에서 s'으로 이동할 확률(Transition probability)
- R : 각 요소가 $r(s) = E[R_{t+1}|S_t=s]$인 집합. r(s)는 상태 s에서 얻는 보상
- $\gamma$ : 즉각적으로 얻는 보상과 미래의 얻을 수 있는 보상 간의 중요도를 조절하는 변수(Discount factor). 0 ~ 1

### 보상
- $G_t$ : 시간 t 이후부터 얻을 수 있는 보상의 합.
- $G_t = R_{t+1} + \gamma R_{t+2} + ... = \sum_{k=0}^{\inf} \gamma^k R_{t+k+1}$

### 상태-가치 함수
- 상태 s에서 시작했을 때 얻을 수 있는 보상의 기댓값
- $v(s)=E[G_t|S_t =s]$
- 목표를 달성하는데 있어 상태가 얼마나 좋은지를 나타냄
- 해당 함수는 재귀 형태로 표현 가능(Bellman equation)
- $v(s) = E[R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ...|S_t=s] = E[R_{t+1} + \gamma v(S_{t+1})|S_t=s]$
- $v(s) = R_{t+1} + \gamma \sum_{s' \in S} p(s'|s)v(s')$
- $v = r + \gamma Pv \Leftrightarrow (I- \gamma P)v=r \Leftrightarrow v=(I-\gamma P)^{-1} r$ 

## 2. MDP
- Markov reward process에 행동이라는 요소 추가. $<S, A, P, R, \gamma>$
- 각 상태마다 전체적인 보상을 최대화하는 행동이 무엇인지를 결정
- 정책, $\pi$ : 각각의 상태마다 행동의 분포를 표현하는 함수. $\pi(a|s)=Pr(A_t = a|S_t = s)$
- MDP가 주어진 정책을 따를 때, 상태 변화식
- $p_{\pi} (s'|s) = \sum_{a \in A} \pi (a|s)p (s'|s,a)$
- 이에 따른 보상식
- $r_{\pi} (s) = \sum_{a \in A} \pi (a|s) r(s,a)$

### State-Value function with policy
- 특정 상태에서 시작했을 때 얻을 수 있는 보상의 기댓값
- $v_{\pi} (s) = E_{\pi} [G_t|S_t=s] = E_{\pi} [R_{t+1} + \gamma v_{\pi} S_{t+1} |S_t=s]=\sum_{a \in A} \pi (a|s) (r(s,a) + \gamma \sum_{s' \in S} p(s'|s,a)v_{\pi} (s'))$

### 행동-가치 함수
- 상태 s에서 시작하여 행동을 취했을 때 얻을 수 있는 보상의 기댓값
- $q_{\pi} (s,a) = E_{\pi} [G_t|S_t=s, A_t=a]=E_{\pi} [R_{t+1} + \gamma q_{\pi} (S_{t+1}, A_{t+1}) | S_t=s]=r(s,a)+ \gamma \sum_{s' \in S} p(s'|s,a) \sum_{a' \in A} \pi (a'|s') q_{\pi} (a'|s')$
- 상태-가치 함수는 어떠한 상태가 더 많은 보상을 얻을 수 있는지를 알려줌. 행동-가치 함수는 어떠한 상태에서 어떠한 행동을 취해야 더 많은 보상을 얻을 수 있는지 알려줌
- 모든 상태에 대해서 행동-가치 함수를 계산할 수 있다면, 모든 상태에 대해 최적의 행동을 할 수 있ㅇ므

### 최적값
- 최적의 상태-가치 함수는 주어진 모든 정책에 대한 상태-가치 함수의 최대값
- $v_* (s)=max_{\pi} v_{\pi} (s)$
- 최적의 행동-가치 함수 또한 모든 정책에 대한 행동-가치 함수의 최대값
- $q_* (s,a) = max_{\pi} q_{\pi} (s,a)$

