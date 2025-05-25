array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 자기보다 작은 값을 만나면 멈춤
        else:
            break
        
print(array)