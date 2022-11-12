# Markov Chain

- 주어진 확률에 따라 변화하는 시스템을 추적하는 특정 모델
- 이산시간 확률 프로세스

<img width="187" alt="캡처" src="https://user-images.githubusercontent.com/80622859/201045396-88acc8a6-d34e-4588-9462-8f3f286f1543.PNG">

- 전이 확률(Transition Probability) : 특정 시간 t동안 특정 상태 i에서 특정한 다른 상태 j로 전이할 확률

![캡처](https://user-images.githubusercontent.com/80622859/201462005-c6c5ffbd-c09f-4037-ad7f-999c011e6228.PNG)

- 전이 확률 행렬 : 모든 상태 조합에 대한 전이 확률을 나타낸 것

![캡처](https://user-images.githubusercontent.com/80622859/201462022-171ab633-d0d4-4ccf-944b-3e024047f747.PNG)

- 시간 t+u의 전이 확률 행렬은 시간 t의 전이 확률 행렬과 시간 u의 전이 확률 행렬의 곱

![캡처](https://user-images.githubusercontent.com/80622859/201462044-8774d794-b267-4e19-81be-18f01cca5e65.PNG)

## 예시
1. 오늘 비가 내리는 경우, 내일 비가 내일 확률은 40%, 비가 내리지 않을 확률은 60%
2. 오늘 비가 오지 않는 경우, 내일 비가 내릴 확률은 20%, 비개 내리지 않을 확률은 80%



