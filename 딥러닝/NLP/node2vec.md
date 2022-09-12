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
- 
