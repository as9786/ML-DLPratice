# 입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 정렬
a.sort()
b.sort(reverse=True)

p = 0

for i in range(len(a)):
    # 교체 횟수를 다 사용했다면 종료
    if p == k:
        break
    # A의 원소 값이 B의 원소값보다 작을 경우 교체
    if a[i] < b[i]:
        a[i] = b[i]
        p += 1
    else:
        continue
    
print(sum(a))
          