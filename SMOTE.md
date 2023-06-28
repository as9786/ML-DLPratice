# SMOTE

## Imbalanced data

![image](https://github.com/as9786/ML-DLPratice/assets/80622859/d7b11d26-9f34-4d18-8a1b-e93be3957f7a)

- Class 별로 train dataset의 크기가 급격히 차이가 나는 data

## Random under sampling

- Majority class에서 임의로 sampling하여 크기를 맞추는 방법
- 임의로 선택된 sample의 대표성이 떨어질 경우 문제생

## Random over sampling
- Minority class의 data를 반복하여 양을 train data의 양으로 맞추는 방법
- Minority class의 가중치를 증가시키는 것

## SMOTE(Synthetic Minority Oversampling Technique)

- k-Nearest neighbor 중, 임의로 하나의 표본을 선택하여 linear combination을 추가
- Random over sampling에 비해 다양한 data를 추가 가능

## Borderline-SMOTE
- 안전한 지역에 있거나, 잡음으로 간주되는 표본은 oversampling 하지 않고, 위험 지역인 경계(borderline)에 있는 표본만 oversampling
- $N_M$ : 주변에 존재하는 majority sample의 수
- Noise sample : $N_M = k$
- Safe sample : $N_M < \frac{k}{2}$
- Danger sample : $\frac{k}{2} \leq k < k$

