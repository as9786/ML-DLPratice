# 초록

- Original transformer의 attention 계산에 memory-access에 관련된 비효율이 존재

<img width="1796" height="1018" alt="image" src="https://github.com/user-attachments/assets/93eb33dc-3c57-4a30-81ae-1115808f018a" />

- GPU에서 연산 시, HBM(GPU main memory)으로의 접근이 너무 많아 입출력 통신이 병목
- 이를 해소하기 위해 불러오기/읽기 과정을 줄이고, SRAM에서 한 번에 계산을 진행(Hardware-Aware programming)

# 1. Standard problem의 문제점
- Query와 key의 상호 작용인 attention map을 계산하여 일종의 pairwise coefficient를 계산
- 그 후, value를 곱해서 해당 층에서 잔차에 연관된 값을 구함

<img width="1252" height="868" alt="image" src="https://github.com/user-attachments/assets/9cb48c9c-cfa7-4cb9-b933-edee6e66d8bc" />

- 위 그림은 CPU와 GPU의 버스 통신 흐름에 따라 계층적으로 나타낸 메모리 구조
- CPU의 main memory에 적재된 값이 GPU의 HBM과 GPU의 SRAM을 차례로 거쳐 적재되었을 때 연산이 진행
- CPU <=> GPU 접근 시간뿐만 아니라 HBM <=> SRAM의 접근 시간도 중요

# 2. Attention 계산
- Q, K, V를 block 단위로 HBM에서 관리하고 SRAM에서 한 번에 계산하도록 하는 것이 핵심
- Softmax 연산을 위해 Q와 K를 행 방향으로 자른 뒤 병합

## 2-1. Titling
- Softmax는 vector의 최대값을 중심으로 크기를 조정
- m : Block x의 최대값, l : softmax(x)를 정규화하기 위한 summation value (Softmax normalization statistics)

$m(x) := max_i x_i$  $f(x) := [e^{x_i - m(x)}, ..., e^{x_B - m(x)}]$ $l(x) := \sum_i f(x)_i$ $softmax(x) := \frac{f(x)}{l(x)}$ 

- Blocks의 l과 m을 활용해 softmax를 계산할 수 있음
- Attention map을 HBM에 저장하지 않고도 순전파, 역전파를 진행 가능

<img width="1260" height="754" alt="image" src="https://github.com/user-attachments/assets/68a54fbb-f133-483b-9978-782e3ace2ec3" />
