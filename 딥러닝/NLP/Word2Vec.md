# Distributed Representations of Words and Phrases and their Compositionality

## Abstract
- Skip-gram : 단어의 syntactic(구문론), sementic 관계를 효율적으로 표현할 수 있는 model
- 구문론 : 의미를 무시하고 기호 사이의 형식적 관계를 취급하는 학문
- 자주 사용되는 단어에 대한 subsampling을 통해 속도 향상과 더욱 규칙적인 단어를 표현 가능
- 계층적인 softmax의 대안을 제시

## Introduction
- Vector space에서 단어의 분산적인 표현은 유사한 단어를 grouping
- Efficient estimaton of word representations in vector space : 많은 양의 text data로부터 양질의 단어 표현을 할 수 있는 skip-gram model 제안. 이전에 사용하던 word vector를 훈련시키기 위해 신경망 구조와 다르게 행렬곱 연산을 사용하지 않음 => 효율적

### Skip-gram
 
![다운로드 (3)](https://user-images.githubusercontent.com/80622859/189517486-d740dfbb-028b-475e-b75b-7b776ae1c51b.png)
