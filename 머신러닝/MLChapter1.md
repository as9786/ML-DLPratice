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
- 주어진 보드 상태에 대해 함수 $\hat V$는 다음과 같은 보드 기능의 선형 조합으로 계산

- $x_1$ : 보드의 검은색 조각 수
- $x_2$ : 보드의 빨간색 조각 수
- $x_3$ : the number of black kings on the board
- $x_4$ : the number of red kings on the board
- $x_5$ : 빨간색으로 위협받는 검은색 조각의 수
- $x_6$ : 검은색으로 위협받는 빨간색 조각의 수

![render](https://user-images.githubusercontent.com/80622859/190848048-c2fbaba2-ebbb-4e6b-a791-6bd556a31fca.png)

- $w_0 ~ w_6$ : Training algorithm에 의해 선택될 수치 계수 또는 가중치
- $w_1 ~ w_6$까지의 학습된 값은 board의 값을 결정하는데 있어 다양한 보드 특징의 상대적 중요성을 결정하는 반면 $w_0$는 보드의 값에 추가 상수를 제공
- 목표 함수 표현에서 계수에 대한 값 학습 문제로

## Choosing a Function Approximation Algorithm
- $\hat V$를 학습하기 위해서는 각각 특정 보드 상태 b와 b에 대한 훈련값 $V_{train} (b)$를 설명하는 일련의 훈련 예제가 필요
- 각 훈련 예제는 $(b,V_{train} (b))$ 형식의 순서 쌍
- ex)

![render](https://user-images.githubusercontent.com/80622859/190848454-9e2848ba-7773-4cd6-b4c3-704ffa414072.png)

### ESTIMATING TRAINING VALUES
- 학습자가 사용할 수 있는 유일한 훈련 정보는 게임이 결국 승리했는지 패배했는지에 대한 여부
- 그러면 중간 보드 상태에 대한 훈련값을 추정하는데 모호함 발생
- 위를 해결하기 위해 임의의 중간 보드 상태 b에 대한 $V_{train}(b)$의 훈련 값을 V(Successor(b))로 할당
- $\hat V$는 V에 대한 학습자의 현재 근사치이고, Successor(b)는 다시 프로그램의 이동 순서인 b에 이은 다음 보드 상태
- 훈련 값 추정에 대한 규칙

![render (1)](https://user-images.githubusercontent.com/80622859/190848661-1f201efe-9ee0-4a55-9d89-52fc203e168b.png)

- 보드 상태 b의 값을 추정하기 위해 후계자의 값을 추정치로 사용

### ADJUSTING THE WEIGHTS
- 가중치를 학습하는 법
- 훈련 값과 가설에 의해 예측된 값 사이의 제곱 오차 E를 최소화하는 것으로 가중치 집합을 정의 

<img width="367" alt="캡처" src="https://user-images.githubusercontent.com/80622859/190848747-2c2fc2c1-565b-47dc-b656-b022fa0be9d1.PNG">

- 관찰된 훈련 예제에 대해 E를 최소화하는 가중치 또는 $\hat V$를 찾음
- 위를 계산하는 algorithm : 최소 평균 제곱 or LMS 훈련 규칙
- 관찰된 각 훈련 예제에 대해 이 훈련 예제의 오류를 줄이는 방향으로 가중치를 조정
- LMS algorithm

<img width="411" alt="캡처" src="https://user-images.githubusercontent.com/80622859/190848803-5f65884d-22ac-4ddc-87ad-f813ddba140d.PNG">

- $\eta$는 가중치 업데이트의 크기를 조정하는 작은 상수(0~1)
- 오류가 0이면 가중치가 변경되지 않음

### The Final Design

<img width="368" alt="캡처" src="https://user-images.githubusercontent.com/80622859/190848866-e543f8f0-d54e-47f0-b241-49ba10b9b99d.PNG">

- Performance System : 학습된 목표 함수를 사용하여 주어진 성능 작업을 해결해야 함. 새로운 문제의 예를 입력으로 취하고 해결책의 추정값을 출력. 다음 동작을 선택하기 위해 학습된 $\hat V$ 평가. 
- Critic : 게임의 역사나 추적을 입력으로 사용하고 목표 함수의 훈련 예제를 출력으로 생성
- Generalizer : 교육 예제를 입력하고 목표 함수의 추정치인 출력 가설을 생성. 이 예제에서 일반화는 LMS. 출력 가설은 $\hat V$
- Experiment Generator : 현재 가설을 입력으로 사용하여 performance system이 탐색할 새로운 문제를 출력. System 전반의 학습율을 극대화할 수 있는 새로운 문제를 뽑는 것. 이 예제에서는 새로운 게임을 시작하기 전 항상 동일한 초기 보드 상태를 제안

- 적어도 대표할 수 없는 것은 절대 배우지 않음
- 선형 함수 표현은 단순해서 좋은 성능은 안 나올 수 있음

# PERSPECTIVES AND ISSUES IN MACHINE LEARNING
- 기계 학습에 대한 한 가지 유용한 관점 : 관찰된 data와 학습자가 보유한 모든 사전 지식에 가장 적합한 것을 결정하기 위해 가능한 가설의 매우 큰 공간을 검색하는 것을 수반
- 서로 다른 가설 표현은 서로 다른 종류의 목표 함수를 학습하는데 적합

## Issues in Machine Learning
- 특정 훈련 사례에서 일반적인 목표 함수를 학습하기 위해 어떤 알고리즘이 존재하는가?
- 데이터가 충분한가?
- 학습자가 보유한 사전 지식은 언제, 어떻게 예제를 통해 일반화하는 과정을 보여주는가?
- 학습 과제를 하나 이상의 함수 근사 문제로 줄이는 가장 좋은 방법?
- 학습자가 목표 기능을 표현하고 학습하는 능력을 향상시키기 위해 표현을 자동으로 변경할 수 있는 방법?

# SUMMARY AND FURTHER READING
- 기계 학습은 다양한 응용 분야에서 큰 실용적 가치가 있음
- 다양한 분야의 idea 활용
- 잘 정의된 학습 문제는 잘 지정된 작업, 성능 metrix 및 훈련 경험의 출처가 필요
- 기계 학습 접근 방식을 설계하려면 훈련 경험의 유형 선택, 학습할 목표 기능, 이 목표 기능에 대한 표현, 훈련 예제에서 목표 기능을 학습하기 위한 알고리즘을 포함한 많은 설계 선택이 수반
- 학습은 탐색을 포함 : 가능한 가설 공간을 탐색하여 사용 가능한 훈련 예시와 다른 사전 제약이나 지식에 가장 적합한 가설을 찾아야 함. 
