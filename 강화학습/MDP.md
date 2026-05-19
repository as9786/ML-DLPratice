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
- $v(s)=E[G_t|S_t=s]$
- 목표를 달성하는데 있어 상태가 얼마나 좋은지를 나타냄
- 해당 함수는 재귀 형태로 표현 가능(Bellman equation)
- $v(s) = E[R_{t+1} + \gamma R_{t+2} + \gamma&2 R_{t+3} + ...|S_t=s] = E[R_{t+1} + \gamma v(S_{t+1})|S_t=s]$
- $v(s) = R_{t+1} + \gamma \sum_{s' \in S} p(s'|s)v(s')$
- $v = r + \gamma Pv \Leftrightarrow (I- \gamma P)v=r \Leftrightarrow v=(I-\gamma P)^{-1} r$ 
