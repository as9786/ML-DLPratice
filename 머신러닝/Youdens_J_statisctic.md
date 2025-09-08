# Youden's J statistic
- 이분법적 진단 검사에서 ROC 분석을 할 때, 특정 cut-off에 따른 진단 검사의 성능을 보여주는 값. Cut-off를 정하기 위한 성능을 평가하는데 이용
- J = sensitivity - (1 - specificity) = 민감도 - (1 - 특이도)
- -1 ~ 1 사이의 값을 가짐. 1에 가까울수록 완벽한 값
- ROC cureve와 y=x 사이의 세로선 길이

<img width="1226" height="1189" alt="image" src="https://github.com/user-attachments/assets/cdd13042-0ecf-48b2-8f1d-1ac86290d8ac" />

- Youden's index를 최대로 하는 cut-off를 찾는 것
- 
