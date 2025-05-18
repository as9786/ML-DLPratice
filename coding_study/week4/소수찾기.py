# Library
from itertools import permutations 
# 소수 판별 함수 
def is_prime(num):
    # 결과값 초기화
    result = True
    # 숫자가 2보다 작을 경우, 소수 아님
    if num < 2:
        result = False
    # 숫자가 2일 경우, 소수
    elif num == 2:
        result = True
    # 이외의 경우
    else:
        for i in range(2, int(num ** (1/2))+1):
            if num % i == 0:
                result = False
                break
        
    return result
        
def solution(numbers):
    answer = 0
    # List type
    num_list = list(numbers)

    # 중복 숫자 확인을 위한 list
    ok_list = []
  
    for i in range(1, len(num_list)+1):
        # 숫자 조합 생성
        permutation_result = list(permutations(num_list,i))
        for pr in permutation_result:
            # 숫자형으로 변환
            check_num = int(''.join(pr))
            # 중복될 경우
            if check_num in ok_list:
                continue
            # 소수 판별 
            if is_prime(check_num):
                answer += 1 
                ok_list.append(check_num)
    return answer
