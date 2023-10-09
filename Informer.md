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

