# 주어진 6개의 카드
card_arr = list(map(int, input().split()))

# Baby-Gin인지 구별하는 함수
def is_baby_gin(card_arr):
    # 0~9만큼의 길이를 가진 배열(10) 만들기
    count_arr = [0] * 12
    is_tri = 0
    is_run = 0
    # 카드의 숫자와 동일한 인덱스를 가진 배열 값 +1
    for i in card_arr :
        count_arr[i] += 1
    
    # 1. TRI 찾기
    # 2. RUN 찾기
    for i in range(len(count_arr)):
        if count_arr[i] >= 3 :
            count_arr[i] -= 3
            is_tri += 1
        if count_arr[i] >= 1 and count_arr[i+1] >= 1 and count_arr[i+2] >= 1 :
            count_arr[i] -= 1
            count_arr[i+1] -= 1
            count_arr[i+2] -= 1
            is_run += 1
    
    # RUN / TRI 여부에 따라 결과 return
    if is_run + is_tri >= 2 :
        return True
    else :
        return False
    
result = is_baby_gin(card_arr)

if result == True :
    print("Yes")
else :
    print("No")