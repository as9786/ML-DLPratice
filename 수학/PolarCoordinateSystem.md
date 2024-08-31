# 극 좌표계 정의
- 일반적으로 좌표계는 Cartesian coordinate system을 사용. 가로축이 x, 세로축이 y축이 되는 형태
- 물체의 이동 및 회전이 동시에 고려되어야 한다면 cartesian coordinate system에서는 회전에 따른 x,y의 변화를 매번 계산해야 하는 불편함 발생
- 회전 동작을 편리하게 사용하기 위해서 고안된 좌표계가 극 좌표계

![image](https://github.com/user-attachments/assets/a59920b8-2212-43a3-b0d8-3732f4c0f06f)

- 위 그림과 같이 원점으로부터 거리 r과 각 $\theta$의 두 요소로 구성되며 극좌표계의 좌표는 $(r, \theta)$로 표시
- 극 좌표계는 동심원의 형태로 평면의 모든 점을 표현할 수 있으며 주로 시간에 따른 회전의 움직임을 구현하기에 용이
- Cartesian coordinate system에서 표현된 vector (x,y)는 vector의 크기와 arctan 함수를 사용하여 다음과 같이 $(r,\theta)$로 변환

![image](https://github.com/user-attachments/assets/d9ff8e55-73ea-4635-89ed-b300465992d2)

- atan2(y,x)는 제 1사분면에서의 atan(y/x)와 같음. 하지만 다른 사분면에서는 부호에 따라 값이 달라질 수 있음
- atan은 두 점 사이의 tan 값을 받아 $-\pi / 2~ \pi /2$ 범우의 radian 값(-90도~90도)을 반환하는 반면, atan2는 두 점 사이의 상대좌표 (x,y)를 받아 $-\pi ~ \pi$ 범위의 radian 값(-180도~180도)의 radian 값을 반환
- 반대로 극 좌표계의 좌표 $(r, \theta)$를 cartesian coordinate system (x,y)로 변환하는 식은 삼각함수를 사용

![image](https://github.com/user-attachments/assets/7d7626d0-dc78-40d6-a6a2-6a45680c1111)

- 위 식들을 이용하면 (x,y)와 $(r,\theta)$ 간의 변환을 자유롭게 할 수 있음

![image](https://github.com/user-attachments/assets/6695b21a-3772-4270-a73b-bf79eace831a)

# 극 좌표계 활용 예시
- 호의 넓이를 구할 때는 극 좌표계를 사용하는 것이 좀 더 편할 수 있음
- 극 좌표계의 사용 목적이 회전 동작을 편리하게 사용하기 위한 것으로 정의하였기 때문
- 부채꼴의 넓이를 구하기 위하여 ds를 적분하는 방식

![image](https://github.com/user-attachments/assets/f08500b8-f800-4c1b-9461-aafa427cc131)

- 호의 길이 변화량과 반지름의 변화량으로 면적의 변화량을 나타낼 수 있음

![image](https://github.com/user-attachments/assets/421ed343-bc4e-4947-99d4-5ef9353d00d3)

- 다음과 같은 직교 좌표계에서의 적분은 사실상 사람이 직접 풀기에는 어려움이 있음

![image](https://github.com/user-attachments/assets/3907d9ca-ef28-4e80-a303-329e0e32b405)

- 위 식에서 x의 범위는 $0~\infty$이고, y의 범위는 $-\infty ~ \infty$. 즉, 직교좌표계에서 1, 4 사분면 전체 영역에 대하여 적분
- 극 좌표계로 변환한다면 r의 범위는 $0~\infty$가 되고, $\theta$의 범위는 -90도에서 90도가 됨

![image](https://github.com/user-attachments/assets/16a4059d-c6cb-460d-8504-60d0e5b3218f)



