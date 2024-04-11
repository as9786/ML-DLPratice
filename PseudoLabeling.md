# Pseudo labeling

- 준지도학습(Semi-supervised learning) : 정답 label을 알 고 있는 data(크기가 작음)로 1차 학습 진행 후, 정답 label이 없는 test data로 2차 학습을 진행하는 학습
- 기존에 정답이 있는 data에 정답이 없는 data를 학습시켜 도출된 결과를 접목시켜서 기존 가지고 있는 정답에 기반항 확률적인 정답을 부여하는 기법

## 방법

1. 정답이 있는 data로 모형 학습
2. 1번에서 학습한 모형을 활용하여 정답이 없는 data를 예측하고, 그 결과를 정답으로 사용하는 pseudo labeled data 생성
3. 2번에서 만든 dataset과 기존 dataset을 사용하여 모형 학습

- Stacking과 유사
- Stacking은 예측한 값을 변수로 그대로 이용
- Pseudo labeling은 정답이 없는 data로 예측하여 도출한 결과와 정답이 있는 data를 가지고 새롭게 학습

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/ed8f1516-3529-48fe-83eb-efa0e64b33c6)

- 기존의 data로 일정 이상의 성능을 보일 때, 사용하는 것이 좋음

## 손실 함수
- Labeled data와 unlabeled data 간의 균형 있는 학습이 중요
- 손실 함수에 상수를 추가하여 둘 사이의 균형을 조절
- a(t)가 균형을 조절해줌

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/034e40d9-7490-466e-a50c-4ad67d0d2f6a)

- a(t)가 너무 클 경우, labeled data에 의한 학습을 방해
- a(t)가 너무 작을 경우, unlabeled data에서 얻는 이점을 활용할 수 없음
- a(t)를 서서히 증가시키면 최적점이 국소점에 빠지는 것을 예방
- 
