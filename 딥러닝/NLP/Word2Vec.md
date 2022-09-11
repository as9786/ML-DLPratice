# Distributed Representations of Words and Phrases and their Compositionality

## Abstract
- Skip-gram : 단어의 syntactic(구문론), sementic 관계를 효율적으로 표현할 수 있는 model
- 구문론 : 의미를 무시하고 기호 사이의 형식적 관계를 취급하는 학문
- 자주 사용되는 단어에 대한 subsampling을 통해 속도 향상과 더욱 규칙적인 단어를 표현 가능
- 계층적인 softmax의 대안을 제시

## Introduction
- Vector space에서 단어의 분산적인 표현은 유사한 단어를 grouping
- Efficient estimaton of word representations in vector space : 많은 양의 text data로부터 양질의 단어 표현을 할 수 있는 skip-gram model 제안. 이전에 사용하던 word vector를 훈련시키기 위해 신경망 구조와 다르게 행렬곱 연산을 사용하지 않음 => 효율적
 
![다운로드 (3)](https://user-images.githubusercontent.com/80622859/189517486-d740dfbb-028b-475e-b75b-7b776ae1c51b.png)

- 해당 논문에서는 이전 skip-gram의 성능을 개선
- 빈도수가 높은 단어를 sub-sampling함으로 훈련 속도를 2~10배 향상
- 빈도수가 적은 단어들의 표현에 대한 정확도를 높일 수 있음
- 계층적인 softmax 대신에 Noise Contrastive Estimation(NCE)를 단순화시켜 skip-gram model에 사용 => 속도 향상, 빈도수가 높은 단어에 대하여 더 나은 표현 가능
- 모든 관용구에 대하여 vector represent => skip-gram의 표현력 향상
- Recursive autoencoders : 결합된 단어로 구성된 문장의 의미를 표현하기 위한 기술. Word vector 대신 phrase vector 사용 가능
- Data-driven approach를 이용하여 다수의 phrases 확인 -> Phrases를 훈련 과정에서 개별적인 token으로 취급
- Phrases vector의 평가를 위해 word와 pharses를 모두 포함하고 있는 analogical reasoning task 
- 단순한 vector의 덧셈으로 의미있는 결과를 만들어낼 수 있음 발견
- ex) Russia + river ~= Volga River
- 언어에 대한 이해 정도를 수학적인 연산을 통해 

## The Skip-gram Model
- 문장이나 문서에서 주변 단어들을 예측하는 단어 표현을 찾는 것
- $w_1, w_2,w_3,...,w_t$에 대하여 log 확률의 평균을 최대화하는 것 

![다운로드 (4)](https://user-images.githubusercontent.com/80622859/189517716-171139d9-bc51-452b-bd7d-fb50f2d78d18.png)

- C : training context의 크기, 크기가 클수록 결과는 좋아지지만 훈련에 소요되는 시간도 증가
- 수식

![render (1)](https://user-images.githubusercontent.com/80622859/189517820-a09f16bb-5ad2-4f5c-8539-d7724efd201b.png)

### Skip-gram example
- window size = 2

![다운로드 (5)](https://user-images.githubusercontent.com/80622859/189517859-57fc84ec-a4dc-421d-b9a2-637ced132698.png)

![다운로드 (6)](https://user-images.githubusercontent.com/80622859/189517869-7990cfa2-53c9-4ab6-8bd7-7fae790712eb.png)

- 단일 은닉층만 존재하는 얕은 신경망
- N : 은닉층의 크기, V : 단어 집합의 크기, W : 입력층과 은닉층 사이의 가중치 행렬, V x N 크기, input word matrix, $W'$ : 은닉층과 출력층 사이의 가중치 행렬, N x V 크기, output word matrix
- $W\,,W'$는 전치 관계가 아닌 서로 다른 행렬이며 학습 전에는 모두 무작위 값을 가짐
- 학습

![다운로드 (7)](https://user-images.githubusercontent.com/80622859/189517953-de06a0f6-8309-4e87-8293-0357e2f8b362.png)

- 손실 함수 : Cross entropy

### Hierarchical Softmax
- Full softmax에 근접하면서 연산을 효율적으로 할 수 있는 방법
- Output node를 W에 대한 확률분포로 대신하여 log(W)에 대한 확률분포를 얻을 수 있음
- Binary tree를 이용해서 W의 output node를 표현
- Tree의 각 leaf nodes는 
