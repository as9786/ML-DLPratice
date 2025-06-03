def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾는 값이 중간값인 경우
    if array[mid] == target:
        return mid

    # 찾는 값이 중간값보다 작은 경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    # 찾는 값이 중간값보다 큰 경우
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target,0,n-1)
if result == None:
    print('찾고자 하는 원소 값이 없습니다.')
else:
    print(result + 1)    
    