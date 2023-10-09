# Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting

- Transformer를 기반으로 long sequence의 시계열 예측
- 연산 복잡도를 낮춤 => 효과적이고 빠르게 예측 가능

## 초록

- Long Sequence Time-series Forecasting(LSTF)는 입력과 출력의 정확한 long-range dependency를 효율적으로 포착할 수 있는 높은 예측 능력을 가진 모형을 필요
- LSTF에 transformer가 가능성을 보임. 다만, 몇 가지 문제 존재
1. 시간 복잡도
2. High memory usage
3. Inherent limitation of the encoder-decoder architecture
- 위의 문제를 해결하기 위해 Informer는 아래와 같은 해결방안 제시
1. ProbSpace self-attention mechanism
2. The self-attention distiling highlights dominating attention
3. The generative style decoder, while conceptually simple, predicts the long time-series sequences at one forward operation

## 서론
- 현존하는 방법론들은 대부분은 short-term 문제를 풀기 위해 고안(48개 이하의 시점)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/b8c7999b-2312-4a8f-9ea3-252a826ad921)

- (b)를 보면 48개 이상의 시점을 갖는 순간부터 MSE의 값이 많이 증가
- 추론 속도도 급히 감소
- LSTF의 주요 과제는 long sequence에 대한 예측 능력 향상
1. Long range alignment 능력
2. Efficient computation for long sequence input and output
- Transformer는 1번에 대해서 우수한 성능
- Maximum path length : 특정 시점에서 과거 시점의 값과 비교할 때 필요한 계산 횟수
- Transformer는 maximum path length의 시간복잡도는 O(1)
- 하지만 transformer 역시 2번을 만족하지 못함(Quadratic 연산과 mememory consumption)

## 선행 연구
- Sparse Transformer
- Reformer
- Linformer
- Transformer-XL and compressive transformer

## 방법
- 현존하는 시계열 예측 방법은 두 가지 존재
1. 고전적 시계열 모형 : 확률 통계적 방법론(Bayesian inference), 기계 학습(ARIMA)
2. Deep learning : RNN

- Informer는 encoder-decoder architecture. Purpose fore LSTF problem

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/ac96157d-47e7-4c20-be20-a56437a21e73)

- 왼쪽 그림은 encoder가 long sequence를 입력으로 받고 있음. ProbSparse self-attention 사용
- 파란색 사다리꼴 부분은 dominating attention을 추출하고, 신경망 크기를 줄이기 위한 self-attention distilling operation을 의미
- 옆에 작은 크기로 복제된 encoder는 모형의 강건성을 증가시키는 역할
- 오른쪽 그림은 decoder가 long sequence를 입력으로 받음. 예측해야하는 부분이 0으로 padding
- Decoder는 해당 입력을 받아 encoder로부터 생성된 concatenated feature map과 encoder-decoder attention을 수행하여 주황색 부분의 출력을 예측

### 1. Efficient Self-attention Mechanism
- Canonical self-attention : 기존의 transformer model이 사용하고 있는 전형적인 self-attention
- Transformer의 scaled dot-product attention
- 
![image](https://github.com/as9786/ML-DLPratice/assets/80622859/bf6e46f5-d71f-4e15-a0a0-8bda9015f3dc)

- Q, K, V의 i 번째 row vector를 의미하는 $q_i, k_i, v_i$는 i 번째 query에 대한 attention은 kernel smoother를 활용하여 다음과 같이 수식이 정의될 수 있음(Kernel smoother는 query와 key의 내적을 근사하는 함수)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/d0ffdd5a-5328-45c2-962c-fb648d0178cd)

- $k(q_i,k_j) : Asymmetric exponential kernel, $\exp(q_i k^T_j / \sqrt{d_k})$를 사용
- Self-attention은 value와 $p(k_j|q_i)$ 확률을 결합하여 출력을 얻음
- 이 과정은 quaratic한 횟수의 dot-product 연산과 $O(L_QL_K)$만큼의 memory usage
- 예측 능력을 향상시키는 데에 주요 한계점
- Self-attention의 확률분포가 희소함
- 이는 대부분의 attention score 값이 대부분 낮다는 것을 의미
- $p(k_j|q_i)$들 중에서 성능에 유의미한 영향을 끼치지 않는 것을 제외하는 selective counting strategies 고안
- 하지만 위의 방법은 heuristic하고, 각 multi-head self-attention을 동일한 전략으로 다루고 있기에 이론적 한계가 있음
- Query나 key를 지정할 때, 임의로 진행하게 됨
- 본 논문은 위의 문제를 해결하기 위해 새로운 접근 방식 제안
- Sparse self-attention은 꼬리가 긴 분포를 가짐

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/d06d5635-548f-404e-93d7-b0e411e3fe4a)

- 이는 소수의 dot-product pairs만이 attention에서 주요한 역할을 함. 다른 dot-product pairs는 trivial attention(영향력이 낮음)

#### 1-1 Query Sparsity Measurement
- Dominant dot-product pairs(유의미한 query-key pairs)의 분포는 균등 분포로부터 상이
- 분포의 유사도는 중요한 query를 구분해내는 지표로 사용될 수 있음
- Kullback-Leibler divergence 사용

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/1518d67b-80ed-45a8-aacd-e36123064f09)

- 마지막 상수항을 제거하고 i 번째 query에 대한 희소성 측정 방법을 아래와 같이 정의(Simpler Kullback-Leibler divergence)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/6a80dc5f-8bca-4251-ad31-0133341ca09a)

- 첫 번째 항 : 모든 key에 대한 Log-Sum-Exp(LSE) 값을 의미. 두 번째 항 : $q_i$의 모든 key에 대한 산술평균
- 만약에 i 번째 query가 위의 식에서 큰 값을 가지게 되면, 그 attention probability p는 보다 다양한 확률 값을 가지게 될 것이고, 유의미한 dot-product pairs를 가질 가능성이 더 높음
- 긴 꼬리분포에서 header 부분에 해당하는 pair가 중요

#### 1-2. ProbSparse Self-attention

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/c9079c94-a9d4-414d-b990-8d60a9108dba)

- $\bar{Q}$ : 같은 크기의 q로 구성된 sparse matrix. M(q,K)를 기준으로 하여 Top-u개의 query만으로 구성
- $u = c \cdot \ln L_Q$, c : sampling factor(초매개변수)
- Multi-head에서 각 head 별로 다른 sparse query-key 쌍을 생성 => 표본 추출로 인한 심각한 정보 손실 방지
- 하지만 이 방법도 quadratic operation => Empirical approximation
- 실제 query sparsity 측정값인 M(q,K) 값의 범위를 제한

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/ad4f7965-3cca-4198-96ee-ee344752660b)

- 위의 보조정리를 활용하여 아래의 근사식 도출

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/cf4a6be6-6a2d-4feb-905a-e8a0773273b2)


### 2. Encoder: Allowing for Processing Longer Sequential Inputs under the Memory Usage Limitation

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/3cc4ae5c-81e7-4196-b52b-0792bd2d53ea)

- raw data의 상수 값은 conv1d를 통해 projection. Global/Local 시간 정보인 stamp 값은 각각 positional embedding을 통해 embedding
- 두 개의 embedding matrix는 더해져 최종적으로 encoder embedding

#### 2-1. Self-attention Distilling
- Conv1d와 max pooling을 사용하여 self-attention distilling을 수행
- j 번째 층에서 (j+1) 번째 층으로 증류되는 과정은 아래와 같음

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/462a2d50-d0bb-487a-8185-b3e74391b8ff)

- AB : Attention Block, kernel-size = 3, stride = 2
- Memory 사용량인 감소되는 효과
- 강건성 향상을 위해 원래 입력의 절반 길이만큼만 입력으로 받는 복제된 encoder 구성

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/49a06164-2151-40a3-b09b-3b128f95f346)

## 3. Decoder: Generating Long Sequential Outputs Through One Forward Procedure

- Generative inference
- Decoder input
  
![image](https://github.com/as9786/ML-DLPratice/assets/80622859/cc878606-d662-4b94-af74-b15d42f3c919)

- $X^t_{token}$ : Start token, $X^t_0$ : Placeholder(target sequence, 0으로 설정)
- Placeholder 부분의 input embedding으로는 시간 정보만 반영
- Masked multi-head attention이 ProbSparse self-attention 계산에 사용

 ### 3-1 Generative Inference
 - Step-by-step inference가 아닌 한 번에 생성이 가능한 decoding

### 3-2 Loss function
- MSE loss

