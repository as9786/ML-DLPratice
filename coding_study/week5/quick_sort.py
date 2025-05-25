array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 한 개인 경우, 종료
    if start >= end:
        return

    # 첫 번째 원소를 pivot으로 설정
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # Pivot보다 큰 값을 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # Pivot보다 작은 값을 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # 엇갈렸다면, pivot을 작은 값으로 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면, 작은 값과 큰 값을 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후, 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)
            