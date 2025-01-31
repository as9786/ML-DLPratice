![image](https://github.com/user-attachments/assets/5f925d7b-a04e-4cc3-8ed3-5c76419d00de)

- 소거법을 통해 위의 연립 방정식을 풀이
- 소거법는 미지수 앞의 계수의 절댓값만 맞추면 소거가 가능

# Pivot
- 한 행에서 일차방정식의 첫 번째 미지수 앞의 계수 또는 기본행연산을 적용하여 행사다리꼴로 변형하였을 때, 대각성분을 pivot이라고 함
1. Pivot은 계수를 바꿔 미지수를 제거할 방정식의 미지수 계수
2. 한 미지수에 대한 pivot은 1개. n개의 미지수를 포함한 연립방정식에서 pivot의 최대 개수는 n개
3. $Pivot \neq 0$

![image](https://github.com/user-attachments/assets/dc319490-b53d-473f-b8d0-09a146f1af52)

- 위 연립 방정식에서 첫 번째 식의 x의 계수는 1이고, 두 번째 식의 x의 계수는 3이므로 pivot=1,3이라고 하면 안 됨
- 1번 정의에 따라야 함
- 하지만 이와 같은 형태에서는 y의 pivot 값을 찾을 수 없고, x의 pivot 값이 두 개인 것처럼 보임
- 1행에 대해서 x에 대한 pivot은 1(y가 제거)
- y의 pivot을 구하기 위해 소거 진행
- (2) - 3 x (1)을 진행

![image](https://github.com/user-attachments/assets/0f4cacbb-acc8-4162-9523-1e853a1e19b2)

- 2행 y에 대한 pivot = 8
- Pivot을 구하는 방법
    1. 미지수를 소거할 방정식(Pivot을 찾을 방정식)을 고름
    2. 그 방정식의 소거할 미지수의 계수를 바로 위 방정식의 pivot으로 나눔. 해당 값을 승수(multiplier)라고 함
    3. 위 방정식 양변에 승수를 곱하고 두 방정식을 더하여 대체. 그 때 소거된 방정식의 첫 미지수 계수가 pivot
- 위 과정을 소거(elimination)라고 함

![image](https://github.com/user-attachments/assets/c37179d0-e91d-4442-89aa-96d99cc7d53d)

- 위 경우의 승수=3. 소거할 미지수의 계수=3, pivot=1, 승수 = 3/1

![image](https://github.com/user-attachments/assets/25e5d36b-e5ec-4544-a40a-954d9ea2a23b)

- 행렬로 변환시 계수행렬 A가 상삼각행렬로 바뀜
- 일반적으로 한 쌍의 해를 가지는 연립방정식의 행렬표현에서 소거법을 진행하면 n행 n열(대각성분) 위치에 pivot들이 놓임. 대각성분 아래는 모두 0으로 채워진 상삼각행렬이 만들어짐
- 소거법 : $Ax=b \implies Ux = b'$

## $Pivot \neq 0$
### 1. 해가 존재하지 않는 경우(불능) 
