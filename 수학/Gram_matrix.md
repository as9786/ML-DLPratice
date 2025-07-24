# Gram matrix
- 1개의 filter를 가진 영상은 [1,h,w]로 표기 가능
- 이를 vectorize -> [1, h x w]
- 1개의 filter에 대한 한 행의 vector
- h x w = 3이라고 가정 시, 표기는 아래와 같이 가능
- $\vec{x} = [x_0, x_1, x_2]$
- Filter가 두 개 시, 아래와 같음
- $$\begin{vmatrix} \vec{x_1} \\ \vec{x_2} \\ \end{vmatrix}$$
