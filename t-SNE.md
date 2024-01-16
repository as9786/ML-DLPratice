# 차원 축소
- 수 많은 특징들을 가지고 있는 dataset을 이용하여 작업을 할 시, 특징 간의 관계를 파악하기 어령ㅁ
- 특징이 너무 적으면 기계 학습 모형의 성능을 저하시키고, 너무 많으면 과적합
- 차원 축소는 중요한 특징들을 남기고 불필요한 특징들을 줄임
- 불필요한 특징의 개수를 줄이면서 복잡한 특징들 간의 관계를 줄일 수 있고, 시각화 가능. 또한 과적합 방지
1. 특징 제거(Feature elimination)
- 특징을 단순히 삭제
- 삭제된 특징들로부터 어떠한 정보를 얻을 수 없음
2. 특징 선택(Feature selection)
- 통계적인 방법을 이용하여 특징들의 중요도 순서를 정함
- 정보 손실(Information loss)이 발생할 수 있으며 동일한 문제를 푸는 다른 dataset에서는 다른 순위가 매겨짐
3. 특징 추출(Feature extraction)
- 새로운 독립적인 특징을 만듦
- 새로 만들어진 특징은 기존에 존재하였던 독립적인 특징들의 결합으로 만들어 짐
- 선형/비선형 방법으로 나뉘어 짐

# t-분포의 의미

- t-분포는 소 표본(n<30)으로 모평균을 추정하고 모집단이 정규분포와 유사함을 알고 있으나 모표준편차를 모를 때 사용
- Student t-분포

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/0bd86515-7389-4638-a87f-aaf095df3b03)

- 표준정규분포와 유사하게 0을 중심으로 좌우 대칭 형태. 표준정규분포보다 평평하고 기다린 꼬리 형태
- 양쪽 꼬리 형태가 두터운 형태
- 표준정규분포보다 분산이 큼
- 자유도에 따라 다른 모양
- 자유도 = 표본의 수 - 1
- 자유도가 커질수록 표준정규분포에 가까워짐
- 대게 자유도가 30이 넘으면 표준정규분포와 가까워짐 -> 표본이 30이 넘어가게 되면 정규분포를 사용하고 표본이 30보다 작으면 t-분포를 사용하는 것이 일반적
- t-분포에서 확률변수를 T로 표현하면 T의 모평균 $$\mu$$의 추정에 사용되는 추정 통계량을 의미
- 이는 표준정규뷴포에서 표준화 변량인 Z와 같이 표본 평균 $$\bar X$$를 변환한 것
- $$T = \frac{\bar X - \mu}{s/\sqrt n}$$
- n : 표본 수, n-1 : 자유도, $$\bar X$$ : 표본 평균, $$\mu$$ : 모평균, s : 표본의 표준편차