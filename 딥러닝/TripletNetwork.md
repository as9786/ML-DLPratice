# Metric Learning

- 단순히 표현을 학습하는 일반적 DL 과정에서 더 확장된 개념
- 목적 : 각 표본을 설명할 수 있는 feature를 추출
- 이렇게 추출된 features는 서로 다른 정보로 구성
- 추출된 feature의 유사성을 검토하여 표본을 분리하는 것이 목적
- 과거 두 표본에 대한 유사성을 검증하는 방법으로 가장 기초적인 방법 : Euclidean distance
- 하지만 성질이 매우 다를 경우가 아니라면 둘 이상의 사이를 분류하는 것에 어려움

# Triplet Network
- 기준 data로부터 근사한 data는 가깝게, 근사하지 않은 data는 멀리 떨어뜨려서 적절한 분리 공간에 배치

![image](https://user-images.githubusercontent.com/80622859/235295712-055ee365-5562-4b37-bc44-e914c22f9f10.png)

- 가중치를 최신화함으로써 가능

![image](https://user-images.githubusercontent.com/80622859/235295735-406f9552-4f00-466b-8ff2-7ecc6c4c725c.png)

- 동일한 CNN에서 기준이 되는 사진(Anchor image)와 이를 비교할 두 개의 사진(positive and negative image)를 사용
- 그리고 기준 사진에 대한 각각의 거리를 계산하고, L2 norm을 적용한 뒤 두 거리 사이의 손실 값을 계산
- Margin을 통해 각각의 거리의 값에 변화를 줌으로써 최적의 손실을 계산

![image](https://user-images.githubusercontent.com/80622859/235295772-193fa16d-5465-4751-b1cf-b6bf6eaad1b0.png)

- 첫째항은 가까울 수록 좋음(0일 수록 좋음), positive distance
- $\alpha$는 margin, 편향과 비슷한 개념
- 두번째항은 negative distance
- Positive distance는 negative distance보다 항상 작아야 함

![image](https://user-images.githubusercontent.com/80622859/235295850-811d8a9a-53fc-435b-856a-2a3f632893b2.png)


