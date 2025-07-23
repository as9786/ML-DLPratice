# Hessian matrix
- 어떤 함수의 2계 도함수들을 이용해 행렬을 만든 것

<img width="527" height="285" alt="image" src="https://github.com/user-attachments/assets/cee1c4a0-8747-482e-bb29-0225f7aa72b4" />

- $\frac{\partial^2f}{\partial x_1 x_2}=\frac{\partial^2f}{\partial x_2 x_1}$이므로 Hessian matrix는 대칭 행렬
- 임계값이 존재하는 경우, 그 임계값에서 Hessian matrix의 고유값들이 모두 양수면 해당 좌표는 극소점. 반대의 경우, 극대점
- 양수와 음수가 모두 존재할 경우, 안장점(어느 방향에서보면 극대값이지만 다른 방향에서 보면 극소값이 되는 점)
