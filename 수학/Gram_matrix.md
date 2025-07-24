# Gram matrix
- 1개의 filter를 가진 영상은 [1,h,w]로 표기 가능
- 이를 vectorize -> [1, h x w]
- 1개의 filter에 대한 한 행의 vector
- h x w = 3이라고 가정 시, 표기는 아래와 같이 가능
- $\vec{x} = [x_0, x_1, x_2]$
- Filter가 두 개 시, 아래와 같음

<img width="211" height="80" alt="image" src="https://github.com/user-attachments/assets/bb77d4fa-2620-48f7-ba95-0677dcb1ed60" />

- F : Number of filters, M : Number of pixels
- F=2, M=3이라고 가정 

<img width="496" height="74" alt="image" src="https://github.com/user-attachments/assets/39b511e2-0e92-462b-ba3f-fb000609e80d" />

- $F_{ik}=z_i (x_k)$
- $F_{ik}$는 $z_i$ filter에 $x_k$ pixel을 넣은 값

<img width="702" height="164" alt="image" src="https://github.com/user-attachments/assets/df66fe48-d87a-4fd3-9c9b-92f374ce3d69" />

- 공분산 행렬과 유사
- Gram matrix는 특정 층 l에 대하여 feature map의 channel 간 상관관계 정보를 얻음
- Style transfer에서 해당 G를 최소화함으로써 유사한 style을 찾고자 함 
