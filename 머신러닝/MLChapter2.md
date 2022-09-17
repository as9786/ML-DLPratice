# Chapter 2 Concept Learning ang the General-to-Specific ordering
- 특정 훈련 사례에서 일반적인 기능을 유도하는 문제는 학습의 핵심
- 범주의 긍정 및 부정 훈련 예제의 샘플이 주어진 일반 범주의 정의를 획득하는 것을 고려
- 개념 학습은 훈련 예제에 가장 적합한 가설을 위해 사전 정의된 잠재적 가설 공간을 검색하는 문제로 공식화 가능
- 일반적으로 가설 공간에 대해 자연적으로 발생하는 구조로 구성

## Introduction
- 많은 학습은 특정 훈련 예시에서 일반적인 개념을 습득하는 것을 포함

## Concept learning
- 입력 및 출력의 예제에서 boolean 값 함수를 추론

## A concept learning task
- ex) 내 친구 Aldo가 가장 좋아하는 수상 스포츠를 즐기는 날들

![캡처](https://user-images.githubusercontent.com/80622859/190855001-33634f05-5a13-4ed4-80d0-dec1705c0c63.PNG)

- 다른 속성의 값들을 기반으로 임의의 날에 대한 EnjoySport의 가치를 예측하기
- 각 가설이 하늘, 공기, 온도, 습도, 바람, 물 및 예측의 6가지 속성 값을 지정하는 제약 조건의 vector
- 모든 값이 이 속성의 허용됨 -> ?
- 속성에 대한 단일 필수 값 -> ex) Warm
- 허용 가능한 값이 없음 -> $\emptyset$

- 일부 instance x가 가설 h의 모든 제약 조건을 만족하면 h는 x를 양의 예로 분류(h(x)=1)
- Aldo가 습도가 높은 추운 날에만 좋아하는 스포츠를 즐긴다는 가설 -> <?,Cold,High,?,?,?>
- 매일이 긍정적 -> <?,?,?,?,?,?>
- 매일이 부정적 -> $<\emptyset, \emptyset,\emptyset,\emptyset,\emptyset,\emptyset>$

- EnjoySport=yes의 날짜 집합을 학습해야 함

### Notation
- Instance set : 개념이 정의되는 항목의 집합, X
- 현재 예제에서 X는 가능한 모든 요일의 집합이며, 각각 하늘, 공기, 온도, 습도, 바람, 물 및 예보 속성으로 표시
- Target concept : 학습해야할 개념 또는 함수, c
- 일반적으로 c는 instance X에 대해 정의된 임의의 boolean 값 함수. 즉 c:X->{0,1}
- EnjoySport = Yes -> c(x) = 1 <-> EnojoySport = No -> c(x) = 0

- Target concept를 학습할 때 학습자는 c(x)와 함께 X의 instance x로 구성된 일련의 훈련 예제를 제시.
- c(x) = 1인 경우 양의 예(positive example) 또는 memebers of the target concept
- c(x) = 0인 경우 음의 예(negative example) 또는 nonmembers of the target concept
- (x,c(x))로 작성, D : 사용 가능한 학습 data
- c의 훈련 data가 주어지면, 학습자가 직면한 문제는 가설 또는 추정
- H :  학습자가 target concept와 관련하여 고려할 수 있는 모든 가능한 가설의 집합
- 일반적으로 H는 설계자의 가설 표현 선택에 의해 결정
- H의 각 가설 h는 X에 대해 정의된 boolean 값 함수, 즉 h: X -> {0,1}을 나타냄
- 목표는 X의 모든 x에 대해 h(x) = c(x)라는 가설을 찾는 것

### The inductive learning hypothesis
- c에 대해 사용할 수 있는 유일한 정보는 훈련 예제 -> 귀납적 학습
- 기본 가정 : 보이지 않는 instance에 대한 최고의 가설은 관찰된 훈련 data에 가장 적합한 가설

#### 귀납적 학습 가설
- 충분히 큰 훈련 예제 집합에 대해 목표 함수를 잘 근사하는 것으로 발견된 가설은 관찰되지 않은 다른 예에 비해 목표 함수를 잘 근사할 것이다

## Concept Learning as search
- 개념 학습은 가설 표현에 의해 암시적으로 정의된 가설의 넓은 공간을 탐색하는 작업
- 이 검색의 목표는 훈련 예제에 가장 적합한 가설을 찾는 것
- Algorithm 설계자는 가설 표현을 선택함으로써 학습할 수 있는 모든 가설의 공간을 암묵적으로 정의한다는 점을 유의해야 함
- ex) Sky의 속성은 3가지 값이라고 정의 => 유한한 가설 공간

### General-to-Specific ordering of hypotheses
- $h_1$ = <Sunny,?,?,Strong,?,?>
- $h_2$ = <Sunny,?,?,?,?,?>
- $h_2$는 instance에 더 적은 제약을 부과하기 때문에 더 많은 instance를 긍정적으로 분류
- $h_1$에 의해 긍정으로 분류된 사례들은 $h_2$에서도 긍정으로 분류
- $h_2$가 $h_1$보다 일반적

- 한 가설이 다른 가설보다 엄격하게 더 일반적인 경우를 고려하는 것이 유용
- 때때로 역이 유용

## FIND-S: Finding a maximally specific hypothesis
- H에서 가능한 가장 구체적인 가설로 시작하여 훈련 data를 잘 다루지 못할 때마다 가설을 일반화

![캡처](https://user-images.githubusercontent.com/80622859/190855838-867706b8-8750-4242-8870-59e60a650e5d.PNG)

![캡처](https://user-images.githubusercontent.com/80622859/190855843-5c62246e-8020-43cd-a6ab-933632bbd3c4.PNG)

![캡처](https://user-images.githubusercontent.com/80622859/190855850-74dd7329-d43a-4248-876e-de51e1dd12af.PNG)

- 주의 사항
- 학습자가 올바른 target concept으로 수렴하였는가?
- 왜 가장 구체적인 가설을 선호하는가?
- 교육 예제가 일관성이 있는가?
- 몇 가지 구체적인 일관된 가설이 있다면 어떤 것일까?

## Version Spaces and the candidate-eliminational algorithm
- FIND-S의 한계를 해결
- FIND-S는 훈련 예제와 일치하는 H의 가설을 출력
- Version space를 구하기 위한 algorithm
- 가장 특수한 가설과 가장 일반적인 가설로부터 시작
- FIND-S와 마찬가지로 instance를 하나씩 적용하여 두 가설 사이에 존재하는 후보 가설들을 줄여나감
- Positive instance와 negative instance 2가지 모두 사용

![캡처](https://user-images.githubusercontent.com/80622859/190856061-686c85e4-bf15-438d-a349-27aa53901276.PNG)

- 새로 적용할 instance가 positive하면 이 instance를 만족시킬 수 있을만큼만 특수 경계인 S를 일반화해나감
- 위의 과정에서 일반 경계인 G에 어긋나는 가설이 있을 경우 해당 조건을 제거
- 반대로 새로 적용할 instance가 negative하면 이 instance가 negative로 분류될 수 있도록 일반 경계 G의 범위를 줄여나감
- 위의 과정에서 S 쪽에 새로 적용되는 instance를 만족시키는 조건이 있다면 이 조건을 탈락 시킴

![캡처](https://user-images.githubusercontent.com/80622859/190856146-13c87ead-40be-4183-815c-ae4e0323e525.PNG)

- 첫 번째 instance를 적용 시 아래와 같이 변동

![캡처](https://user-images.githubusercontent.com/80622859/190856170-d64d1da3-6d1a-4ae1-bf84-f1d503367c4b.PNG)

- 첫 번째 label이 '예'이므로 이에 맞게 S를 조정하고 G는 거스르는 부분이 없으므로 그대로 유지
- 두 번째 instance 적용

![캡처](https://user-images.githubusercontent.com/80622859/190856212-7f2a95ac-92cd-4526-9079-74f1fef3b4cf.PNG)

- 여기까지는 FIND-S와 동일(Yes만 나왔기 때문
- 세 번째 instance 적용

![캡처](https://user-images.githubusercontent.com/80622859/190856251-fb5fafef-994c-4727-adcc-3ce113e185d2.PNG)

- 하늘, 온도, 일기 예보 세 가지 특성에서 다른 값을 나타냄
- 마지막으로 네 번째 instance

![캡처](https://user-images.githubusercontent.com/80622859/190856282-574db9f0-a008-4ad7-ba2f-ac3f89dabdac.PNG)

- S쪽은 해수 온도와 일기 예보에서 기존 가설과 네 번째 instance 특성값이 다르므로 '?'로 처리
- G쪽은 네 번째 instance에서 일기 예보의 특성값이 가변적임에도 label이 '예'dlamfh (?,?,?,?,?,일정함)에 해당하는 가설을 탈락시킴

## REMARKS ON VERSION SPACES AND CANDIDATE-ELIMINATION

### Will the CANDIDATE-ELIMINATION Algorithm Converge to the Correct Hypothesis? 
- 훈련 예제에 오류가 없고, 목표 개념을 정확하게 설명하는 H 가설이 있다면 목표 개념을 정확하게 설명하는 가설로 수렴
- 목표 개념은 S와 G 경계 집합이 동일한 단일 가설로 수렴할 때 정확히 학습

## INDUCTIVE BIAS

### A Biased Hypothesis Space
- 가설 공간에 알 수 없는 대상 개념이 포함되어 있는지 확인
- 분명한 해결책은 모든 가능한 가설을 포함하도록 가설 공간을 풍부하게 하는 것

### An Unbiased Learner
- 일반적으로 집합 X의 모든 부분집합의 집합을 X의 거듭제곱 집합이라고 함
- Instance의 모든 부분 집합을 나타낼 수 있는 새로운 가설 공간 H'을 정의 함으로써 학습 과제를 편향되지 않은 방식으로 재구성 가능
- 이 가설 공간을 사용시 목표 개념을 표현할 수 없을 수 있다는 걱정 없이 후보 제거 알고리즘을 사용 가능
- 하지만 완전히 일반화할 수 없음

### The Futility of Bias-Free Learning
- 귀납적 학습은 어떤 형태의 선행 가정 또는 귀납적 편향을 요구
- 후보-제거 알고리즘의 귀납적(유도) 편향 : 목표 개념 c는 주어진 가설 공간 H에 포함된다
- 귀납적 편향의 관점에서 보는 것의 장점 
1. 관찰된 데이터를 넘어 일반화하기 위해 정책을 특성화하는 비절차적 수단 제공
2. 귀납적 편향의 강도에 따라 다른 학습자를 비교할 수 있음

- 더 강하게 편향된 방법은 더 많은 귀납적 도약을 만들어 보이지 않는 instance에 더 큰 비율을 부여

## SUMMARY AND FURTHER READING
- 개념 학습은 잠재적 가설의 사전 정의된 큰 공간을 탐색하는 문제로 캐스팅될 수 있음
- 모든 개념 학습 문제에 대해 정의할 수 있는 가설의 일반 대 특정 부분 순서는 가설 공간을 통해 검색을 구성하는 데 유용한 구조를 제공
- FIND-S 알고리듬은 이 일반 대 특정 순서를 사용하여 부분 순서 중 한 가지를 따라 가설 공간을 통해 특정 대 일반 검색을 수행하여 훈련 예제와 일치하는 가장 구체적인 가설을 찾음
- 후보 제거 알고리듬은 이 일반 대 특정 순서를 사용하여 최대 특정(S) 가설과 최대 일반(G) 가설 집합을 점진적으로 계산하여 버전 공간(훈련 데이터와 일치하는 모든 가설 집합)을 계산
- 귀납적 학습 알고리듬은 다른 가설보다 하나의 일관된 가설을 선택하기 위한 암묵적 귀납적 편향 때문에 보이지 않는 예를 분류할 수 있음
-만약 가설 공간이 인스턴스의 모든 가능한 부분 집합(인스턴스의 거듭제곱 집합)에 해당하는 가설이 있는 지점까지 풍부해진다면, 이것은 후보 제거 알고리즘에서 유도 편향을 제거. 불행하게도, 이것은 또한 관찰된 훈련 예제를 넘어 모든 인스턴스를 분류하는 능력을 제거한다. 편견 없는 학습자는 보이지 않는 예를 분류하기 위해 귀납적 도약을 할 수 없음.
