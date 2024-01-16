# 할당 문제(Assignment problem)
- $i \in I$가 $j \in J$에 할당될 때 들어가는 비용을 c(i,j)라고 함
- I에서 J로 가는 일대일 대응(bijection) $sigma$ : I -> J 중에서 가장 비용이 적은 것을 찾는 것

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/b37ab596-805b-4c18-a288-1ead5804474a)

- 위의 식을 최소화 시키는 $\sigma$를 구하는 것
- 해당 문제를 graph로 생각 가능
- i와 j를 잇는 간선을 만들고 그것의 비용을 c(i, j)로 설정
- I는 모두 할당되어야 하며, J는 하나의 i와 사상되어야 함
- 모든 정점이 참여를 하여야 하므로 perfect matching을 찾아야 함

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/2e603cb0-efdb-4d13-a5e5-c88681f7799e)

- 위의 식이 가장 작아지는 perfect matching M을 찾는 것이 목표
- I를 학생, J를 프로젝트라고 가정

||NLP|CV|추천|
|---|---:|---:|---:|
|규찬|3|8|9|
|형훈|4|12|7|
|성주|4|8|5|

- 규찬이 NLP 프로젝트를 받으면 약 3의 비용이 발생
- 먼저 규찬이의 경우를 살펴보면, 어떠한 project를 받아도 3의 비용이 발생
- 그러므로 각각의 비용의 3을 빼줘도 선택 자체에는 큰 변화가 없음
- 이를 모든 학생에게 적용

||NLP|CV|추천||
|---|---:|---:|---:|---:|
|규찬|0|5|6|3|
|형훈|0|8|3|4|
|성주|0|4|1|4|

- 해당 작업을 학생뿐만 아니라 모든 project에 대해서도 적용

||NLP|CV|추천||
|---|---:|---:|---:|---:|
|규찬|0|1|5|3|
|형훈|0|4|2|4|
|성주|0|0|0|4|
||0|4|1||

- 해당 행렬은 모든 원소의 값이 0 이상
- 0의 값을 가지는 학생-projet 쌍만 가지고 모든 학생을 서로 다른 작업에 할당하면, 이는 가장 적은 비용이 발생
- 하지만 위의 행렬의 경우 그럴 수 없음(쾨니그의 정리)

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/5d886e0c-c832-4304-a6ca-56fe8cd9dec1)

- 쾨니그의 정리에 의해 graph에서 maximum-size matching은 minimum-size vertex cover와 동일
- 위의 graph에서는 vertax cover의 크기가 2인 경우 존재
- 
