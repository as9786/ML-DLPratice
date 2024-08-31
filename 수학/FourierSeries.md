# 1. 급수

- 수열의 모든 항을 더한 것. 수열의 합

# 2. Fourier Series

- 아무리 복잡한 함수라도 그것이 주기를 가진다면 단순한 파동들의 조합을 합하여 표현 가능

![image](https://github.com/user-attachments/assets/5f35bd2e-119a-4346-8206-2dd2dbe03da8)

- 첫 번째부터 네 번째까지 단순한 주기함수의 합을 통해 마지막 복잡한 주기 함수를 표현할 수 있음
- 무한하게 다양한 주파수(frequency)를 가진 좌표평면 위에서 주기적인 모향을 갖는 개곡선(정현파)를 각각 얼마나 가중해서 더해주냐에 따라 모든 복잡한 주기함수를 표현 가능

## 2-1. 수식

- ![image](https://github.com/user-attachments/assets/da6e524e-02b9-457d-957e-e64fe8db3230)

- - f(t) : 근사 또는 표현하고 싶은 복잡한 주기 함수
  - t : 연속 변수
  - T : 함수 f의 시간 주기
  - $C_n$ : 계수
  - $e^{j\frac{2\pi n}{T}t}$ : 복잡한 함수를 구성하는 간단한 주기 함수
  - n : 다른 주파수를 가진 sin, cos을 나타내기 위한 정수배
  - j : $\sqrt{-1}$
  
- Fourier series는 다른 주파수를 가진 정현파 함수/신호(sinusodial function/signal)의 합
- Fourier series 식에서 $w=\frac{2\pi}{T}$ 각 주기함수의 주파수를 w라고 가정
- $e^{j\frac{2\pi n}{T}t} = e^{jnwt}$
- $e^{jnwt}=cos(nwt)+jsin(nwt), Euler's formula$
- 위와 같은 급수식으로 변환 가능

![image](https://github.com/user-attachments/assets/ddf02be2-5cd3-4ae2-b9ff-26efed874b9f)

- 적절한 계수($C_n$)를 곱한 다양한 주파수(nw)의 sin과 cosine 함수의 합

### 장점
- 다른 주파수의 다양한 정현파의 합을 통해 어떠한 주기 함수든 표현 가능
- 어느 함수든 주기성을 가지면 Fourier series로 나타낼 수 있음

## 2-2. 모든 주기 함수를 근사한다는 증명
- Fourier series는 단순한 주기 함수의 직교성(orthogonality)을 이용
- 일반적으로 두 vector를 내적하여 0일 때, 두 vector는 직교성을 가짐
- 두 개의 vector로는 3차원 표현 불가능
- 모든 점을 표현하기 위해서는 직교하는 축(dimension)의 개수를 무한히 늘리면 됨

## 2-3. 함수의 직교성
- Fourier series에 vector의 축 개념과 유사하게 적용 가능
- 다양한 주파수를 가진 단순하 주기함수(축) 간의 직교성을 증명하면 그들을 조합하여 모든 주기 함수를 나타낼 수 있음

### 
