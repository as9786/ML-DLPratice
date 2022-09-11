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
