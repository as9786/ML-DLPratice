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

### 복소 함수의 내적
- 함수의 직교성 또한 vector orthogonality와 유사
- 함수의 내적 결과가 0일 경우 직교성을 가지고 있음
- Vector와 다른 부분은 함수는 연속적이기 때문에 함수 곱을 적분해주어야 함(Vector는 곱의 합을 사용)
- 함수에서는 서로 직교할 수 있는 함수가 무한개가 존재하며, 직교하는 함수 집합을 orthogonal set이라고 함
- 구간 [a,b]에서 $f_n (t)=$Orthogonal Set이라면, 임의 함수 $f(t)=\sum_{n=-\infty}^{\infty} c_n f_n (t)$로 표현 할 수 있음
- 이를 fourier series에 적용

![image](https://github.com/user-attachments/assets/d92fc8a3-a165-4bce-94af-8b0a0d263a38)

- 구간 [0,T]에서 서로 다른 정수배 n=p,q에 대하여 $e^{j\frac{2\pi n}{T}t}$가 서로 직교하는지를 증명

![image](https://github.com/user-attachments/assets/6bf7943d-c253-4532-a3d3-d4f103798dcd)

- 복소함수를 내적하려면 켤레 복소 함수를 이용해야 함으로 j앞에 음수를 붙여야 함
- p와 q는 정수이며, 각 주기함수는 다른 주기성을 가짐

![image](https://github.com/user-attachments/assets/34f7c1ac-0111-4e49-aec7-6489e2d70e38)

- $exp(j2\pi (p-q)t)$ 함수의 주기성은 항상 $2\pi$이기 때문에 결과값은 항상 1이 나옴(복소평면에서 euler's rule을 적용)
- 그 결과, $exp(j2\pi (p-q)t)-1=0$이 되어 모든 t에 대해 0이 됨
- 서로 다른 주기성의 정현파로 이루어진 복소 함수들을 서로 직교

## 2-4. Fourier coefficient
- 계수를 찾기 위해서는 앞서 증명한 직교성을 활용
- 내적의 개념을 활용

![image](https://github.com/user-attachments/assets/1468ec23-0f19-4f87-bdf4-4bd25129cc7d)

- 내적할 때처럼 f(t)에 $exp(-j\frac{2\pi q}{T}t)$를 곱한 뒤에 f(t)의 시간 주기인 [0,T] 범위에서 적분

![image](https://github.com/user-attachments/assets/0a5e107e-8331-4b35-b541-19e24610c882)

- 적분과 sigma의 자리를 바꿈
- 적분은 t에 대해서만 하기 때문에 $C_n$은 이와 관련없음으로 앞으로 빼냄
- 적분 부분은 앞의 내적 증명 수식과 동일. 즉, n=p(q와 다른 수)이면 전체 적분이 0이 되어 수식 또한 0의 값을 가짐
- 만약, n=q이면 적분부분이 $\int_{0}^{T} 1dt=T$가 됨
- n=q일 때만 값이 살아남음

![image](https://github.com/user-attachments/assets/7ede2716-1e91-47cf-99ec-66aa8ac5f57a)

# 정리
- Fourier series는 주기성을 가진 주기 함수의 근사만 가능




