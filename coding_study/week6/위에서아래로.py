import sys 
input = sys.stdin.readline

# 입력
n = int(input())
array = [int(input()) for _ in range(n)]

# 정렬
array.sort(reverse=True)

# 출력
for a in array:
    print(a, end=' ')
