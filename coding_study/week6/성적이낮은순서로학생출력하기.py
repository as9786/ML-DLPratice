# 입력
n = int(input())

score_dic = {}

for _ in range(n):
    k, v = input().split()
    score_dic[k] = int(v)
    
# 성적 순으로 정렬
sorted_score_dic = sorted(score_dic.items(), key=lambda x : x[1])

for k, v in sorted_score_dic:
    print(k, end=' ')