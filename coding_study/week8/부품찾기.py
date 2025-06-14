# 이진 탐색
def binary_search(array, target, start, end):

    while start<=end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None 

# 가게의 부품 입력
n = int(input())
# 가지고 있는 부품
a = list(map(int, input().split()))
# 손님이 찾는 부품 수
m = int(input())
# 손님이 찾는 부품
b = list(map(int, input().split()))

# 정렬
a.sort()

print(a)
print(b)

for i in range(m):
    result = binary_search(a, b[i], 0, n-1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')

