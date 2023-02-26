# 합성곱 연산과 Image filter

## Analog 신호 처리

- 선형 시불변 시스템(Linear Time Invariant System, LTI System)
- 선형적이고 시간에 영향을 받지 않는 신호처리 system
- Ex) Noise가 들어왔을 때, noise를 제거후 출력
- t0, t5의 결과값은 같음

## Dirac delta function

![image](https://user-images.githubusercontent.com/80622859/221397280-9d45c752-5e7a-4d22-b78f-76f4d2bdd0cc.png)

- t=0을 제외한 모든 위치에서 출력이 0
- 모든 구간에서 적분한 값은 1

## Impulse Response

![image](https://user-images.githubusercontent.com/80622859/221397318-93ee462d-241c-4d7d-b45c-230cdb0a1508.png)

- 매우 짧은 신호에 대한 출력
- LTI system에 impulse를 입력했을 때의 출력을 impulse response라고 함
- Filter라고도 하며, LTI system의 동작을 표현

## 합성곱 연산(Convolution)

- 두 함수를 합성하는 합성곱 연산
- 한 함수를 뒤집고 이동하면서, 두 함수의 곱을 적분하여 계산
- LTI system에 적용
- LTI system = 입력 신호에 impulse response를 합성곱한 결과

## 2차원 신호와 image

- 흑백 영상은 각 pixel이 0~1 사이의 실수로 된 2D signal로 표현 가능
- 행렬에 표현
- Color image는 RGB의 3 channel로 구성된 2D signal

## 영상의 합성곱 계산

![image](https://user-images.githubusercontent.com/80622859/221397535-f30bace3-4cdd-45f5-a4f5-eeacd1f623dd.png)


- 2D digital signal의 합성곱은 filter를 한 칸씩 옮기면서 영상과 겹치는 부분을 모두 곱해서 합

## 잡음 제거 filter

![image](https://user-images.githubusercontent.com/80622859/221397569-fd1c962c-a56a-4f5b-be18-759c07ed68a0.png)

- 2D Gaussian filter를 적용하며 흐려진 영상을 얻을 수 있음
- 영상이 흐려지는 대신 잡음을 제거하는 특성

## 미분 filter

![image](https://user-images.githubusercontent.com/80622859/221397617-d0b27756-8ac0-47c4-b013-aea593d3652f.png)

![image](https://user-images.githubusercontent.com/80622859/221397621-9cfa22c6-6d85-431d-97bb-ef6b009cb992.png)

- Sobel filter를 적용하면 특정 방향으로 미분한 영상을 얻을 수 있음
- 해당 방향의 edge 성분을 추출
- 
