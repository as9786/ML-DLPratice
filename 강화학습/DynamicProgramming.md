# Dynamic Programming

## Planning & Learning

### Planning
- 환경에 대한 모형을 가지고 있는 경우, MDP에 대한 full knowledge를 가지고 있게 됨
- 이를 planning이라고 하며, MDP의 정보를 기반

### Learning
- 환경의 모형은 모르지만 상호작용을 통해서 문제를 푸는 것

### Process of Planning

#### 예측
- 입력 MDP <S,A,P,R, $\gamma$ > 그리고 정책($\pi$)
- 또는 $MRP < S, P^{\pi}, R^{\pi}, \gamma>$
- 출력 : 가치 함수

#### For control
- 입력 : MDP <S,A,P,R, $\gamma$ >
- 출력  최적의 가치 함수와 최적의 정책

## Dynamic Programming 조건

1) Optimal substructure : 작은 문제로 나뉠 수 있어야 함
2) Overlapping subproblems : 한 sub problem을 풀고 나온 해결책을 저장해(cached) 다시 사용할 수 있음

- MDP는 위 조건을 만족(Bellman equation is recursive, 가치 함수는 작은 문제들의 해)
- $v(s) = E[R_{t+1} + \gamma v(S_{t+1}) | s_t = s]$

## Policy iteration
1. 정책을 임의로 초기화
2. 아래 조건이 될 때까지 반복
- $V=V_{\pi}$라고 할 때,
- For each state s, let $\pi(s) = arg max_{a \in A} \gamma\sum_{s'\in S}P_{sa}(s')V^*(s')$
- 가치 함수에 대해 탐욕적인 정책 최신화 방법이라고 부름
- 정책 반복 역시 poliynomial time 안에 최적의 정책으로 수렴하게 됨

### Policy evaluation
- $v_{\pi}$를 추정
- 반복적으로 정책 평가

### Policy improvement
- $\pi' \geq \pi$를 생성
- 탐욕적인 정책 향상

## Value iteration
1. 모든 s에 대해서 V(s)=0으로 초기화
2. 

