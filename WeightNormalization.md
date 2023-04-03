# 가중치 정규화

![image](https://user-images.githubusercontent.com/80622859/229457680-690008de-12f0-4d96-9f8a-2baac5b04508.png)

- 전결합 계층의 w는 방향과 크기를 같이 학습하지만, 이를 분리하여 g와 v로 나누어 학습
- 학습 시 자유도가 개선되어 최적화가 더 쉽게 이루어짐
- 학습 시 합성곱 신경망에서 batch normalization 대비 연산량이 매우 감소
