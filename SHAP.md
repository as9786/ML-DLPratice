# 1. Game Theory

- 여러 주제가 서로 영향을 미치는 상황에서 서로가 어떤 의사결정이나 행동을 하는지에 대해 이론화
- 개인은 전략을 통해 이득
- 서로에게 영향

## Kind of game

### 협력
- 정보제공
- 전략
- Zero-sum

### 비협력
- 정보비제공
- 전개형
- Non zero-sum

### 협력 또는 비협력
- 규칙을 알고 있는가
- 동시 또는 교대
- 이득과 손실이 같은지 다른지

# 2. Shapley value
- 선형 모형에서는 중요한 변수를 쉽게 알 수 있음(선형 모형은 인과성을 가지고 있음)
- Shapley value는 총 지불금에 각 선수들의 기여도에 따라 선수의 지불금을 정의
- Game : 하나의 관측치에 대한 예측
- 이득 : 모든 data로부터 얻은 평균 예측값에서 하나의 관측치로부터 얻은 예측값을 뺀 값
- 선수 : 예측값을 얻는데 사용한 특성
- 모든 가능한 조합에 대해서 하나의 특성 기여도를 종합적으로 합한 값
- 평균 예측값 : y, 변수 : a,b,c, c의 기여도를 평가(c는 0 또는 1의 값을 갖는 범주형 변수)
- 하나의 표본 추출. a + b + (c=0)과 a + b + (c=1)의 예측값을 비교

