# Scalable feature learning for networks

## Abstract
- 현재의 기능 학습 접근 방식은 network에서 관찰된 연결 pattern의 다양성을 포착하기에는 충분히 표현적이지 않음
- Network의 node들의 연속적인 특징 표현을 위한 framework = node2vec
- Node의 network 이웃을 보존할 가능성을 최대화하는 기능의 저차원 공간에 대한 node의 mapping을 학습
- Node의 network 이웃에 대한 유연한 개념을 정의하고 다양한 이웃을 효율적으로 탐색하는 편향된 무작위 보행 절차 설계


## Introduction
- Network 분석에서 많은 중요한 작업은 node와 edge에 대한 예측을 포함
- Network에서 가장 가능성이 높은 nodel label을 예측하는데 관심
- 한 쌍의 node가 그들을 연결하는 edge를 가져야 하는지 여부를 예측 ex) Social network에서 실제 친구 식별
- Node와 edge에 대한 feature vector를 구성해야 함

![캡처](https://user-images.githubusercontent.com/80622859/189596877-76c19d41-63b9-4377-ab6c-455f4bbdbbfa.PNG)

- Node U와 $s_1$이 동일한 촘촘하게 짜여진 node community에 속하는 것을 관찰할 수 있는 반면, 두 개별 community's node U와 $s_6$는 hub node의 동일한 구조적 역할을 공유
- Real-world networks commonly exhibit a mixture of such equivalences
- 따라서 동일한 network community에서 node를 내장하는 표현을 학습할 수 있을뿐만 아니라 유사한 역할을 공유하는 node가 유사한 embedding을 갖는 표현을 학습할 수 있는 두 가지 원칙을 준수하는 유연한 algorithm을 허용해야 함

### present work
- SGD를 사용하여 사용자 지정 graph 기반 목적 함수를 최적화
- d차원 feature space에서 node의 network 이웃을 보존할 가능성을 최대화하는 feature representation을 반환
- Use a 2nd order random wakl approach to generate network neighborhoods for nodes
- Key : defining a flexible notion of a node's network neighborhood
- node2vec은 적절한 이웃 개념을 선택함으로써 network의 역할 및 속한 community를 기반으로 node를 구성하는 표현을 학습
- 이전 작업을 일반화하고 network에서 관찰된 동등성의 전체 spectrum modeling
- 개별 node의 feature representation이 pairs of noded(edge)로 확장 -> Node뿐만 아니라 edge까지 포함하는 예측 작업
- 두 가지 예측 작업
1. 모든 node에 하나 이상의 class label이 할당되는 multi-label classification
2. Node 쌍이 주어진 edge의 존재를 예측하는 link prediction task

## Related Work
- Graph의 다양한 행렬표현
- Laplacian and the adjacency matrices

### Laplacian
- 일차 미분

![img](https://user-images.githubusercontent.com/80622859/189599856-a84edf1a-0076-4afe-8c7a-3d0ba4d1612c.png)

- 2차 편미분

![다운로드](https://user-images.githubusercontent.com/80622859/189599900-d88228fd-afb9-4278-b6bd-1b52e22f418b.png)

- 2차 미분

![img (1)](https://user-images.githubusercontent.com/80622859/189599935-c3f7da1d-de5b-46fa-8122-f7f3a241ddba.png)

- 이차 미분을 나타내는 연산자는 $\nabla^2$이며 라플라시안 또는 델타 스퀘어라고 읽음
- Laplacian Operator

![다운로드 (1)](https://user-images.githubusercontent.com/80622859/189600328-cfd0ef68-115c-493b-a1a5-0e5aa6ec6305.png)

- 선형(PCA) 및 비선형(IsoMap) 차원 축소 기법은 계산 효율성 측면에서 안 좋고, 다양한 pattern에 강하지 않음
- Skip-gram model
- 문서의 단어를 scan하고 모든 단어들을 포함시켜 단어의 특징들이 가까운 단어들을 예측할 수 있도록 하는 것이 목표
- 단어 특징 표현은 negative sampling과 함께 SGD를 사용하여 우도 목표를 최적화
- Skip-gram model의 영감을 받아 network를 문서로 표현함으로써 network에 대한 유추 확립
- 문서가 단어의 집합인 것과 같은 방식으로, 기본 network에서 node 순서를 sampling하고 network를 순서 있는 node 순서로 바꿀 수 있음


## Feature Learning Framework
