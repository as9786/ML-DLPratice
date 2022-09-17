# Introduction
- Data mining으로 알려진 분야에서 기계 학습은 장비 유지보수 기록, 대출, 금융 거래, 의료 기록 등을 포함하는 대규모 상용 DB에서 귀중한 지식을 발견하기 위해 일상적으로 사용됨
- ex) 음성 단어 인식, 폐렴 환자의 회복률 예측, 신용카드 부정 감지 등

# WELL-POSED LEARNING PROBLEMS
- 기계 학습 : 경험 E에 따라 T의 작업 성능이 향상되면 경험 T와 성능 측정 P의 일부 클래스에서 경험 T로부터 배운다고 한다
- ex) 구어체 인식, 자율주행자, 새로운 천문학적 구조, learning to play world-class backgammon

## A checkers learning problem:
- 작업 T : Playing checkers
- 성과 측정 P : 상대방을 상대로 이긴 경기 비율
- 훈련 경험 E : 자신과의 연습 게임

- 기계 학습에 미치는 영향의 일부 분야와 예 : 인공지능, Bayesian methods, 계산 복잡도 이론, 제어 이론, 정보 이론, 철학, 심리학과 신경생물학, 통계학 

- 관심사 : 학습 문제와 process의 기본 구조

# DESIGNING A LEARNING SYSTEM
- checker game

## Choosing the Training Experience
- 첫 번째 설계 : 학습할 교육 경험의 유형 선택
- 훈련 경험의 유형은 학습자의 성공 또는 실패에 상당한 영향을 미침
- 핵심 속성 : 훈련 경험이 수행 system에 의해 이루어진 선택과 관련하여 직접적 또는 간접적 feedback을 제공하는 여부
- 직접 훈련이 간접 훈련보다 배우는 것이 쉬움
- 핵심 속성2 : 학습자가 훈련 예제의 순서를 제어하는 정도
- 핵심 속성3 : 최종 system 성능 P를 측정해야 하는 예제의 분포를 얼마나 잘 나타내는지
- 학습은 훈련 예제가 향후 시험 예제와 유사한 분포를 따를 때 가장 신뢰할 수 있음
- 현재 대부분의 기계 학습은 훈련 예제의 분포가 시험 예제의 분포와 동일하다는 가정에 기초
- 가끔식 위의 가정이 위반되어야 할 때도 있음

- 학습 system 설계 완료시 필요한 것
1. 정확한 유형의 지식
2. 이 목표 지식에 대한 표현
3. A learning mechanism

## Choosing the Target Function
- 정확히 어떤 유형의 지식을 학습할 것인지, 그리고 이것이 수행 program에 어떻게 사용될 것인지 결정 
- Target function : V: B -> $\mathbb{R}$ 
- V가 집합 B에서 어떤 실제 값으로 board 상태를 mapping
- 목표 함수 V가 더 나은 board 상태에 더 높은 점수를 할당
- System은 V를 학습 -> 현재 board 위치에서 최상의 이동을 선택
- 임의의 board b에 대한 목표값 V(b)를 아래와 같이 정의

1. 만약 b가 이긴 상태 -> V(b) = 100
2. 만약 b가 진 상태 -> V(b) = -100
3. 만약 b가 그려진 최종 상태 -> V(b) = 0
4. 만약 b가 최종 상태가 아니라면 -> V(b) = V(b'). b'은 b에서 시작하여 게임이 끝날 때까지 최적으로 플레이할 수 있는 최고의 최종 board 상태

- 게임이 끝난 상태가 아닌 V(b)(4번 경우) 값을 결정하려면 최적의 play line을 미리 탐색해야 함
- 4번의 경우 게임이 끝날 때까지 효율적으로 계산되지 않기 때문에 비작동적(nonoperational) 정의라고 말함
- 이 경우 학습의 목표는 V에 대한 작동 설명
- 완벽한 V를 예상하기 어려움 -> 함수 근사치
- $\hat V$ : 실제로 학습한 함수, V : 이상적인 목표 함수

## Choosing a Representation for the Target Function
