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

|샘플||NLP||CV||추천|
|---||---||---||---|
|규찬||3||8||9|
|형훈||4||12||7|
|규원||4||8||5|

|제목|내용|설명|
|------|---|---|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|
