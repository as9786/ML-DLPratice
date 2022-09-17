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
