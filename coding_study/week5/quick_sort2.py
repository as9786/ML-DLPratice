array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # List가 하나의 원소만 가지고 있을 경우
    if len(array) <= 1:
        return array
    
    # 첫 번째 원소 pivot으로 설정
    pivot = array[0]
    # Pivot을 제외한 list
    tail = array[1:]
    
    # 분할
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))