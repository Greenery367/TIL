# 함수 : 나만의 명령어 만들기
# ex: a와 b를 입력받으면 이 두 변수를 더해라
# ex: 리스트를 입력받고 각 element의 최대값을 구해라

def sum_2_nums (a, b) :
    c = a + b
    print(c)
    return c

def find_biggest_num (a) :
    big_num = 0
    for i in range (0, len(a)-1) :
        if big_num < a[i] :
            big_num = a[i]
            print(f"{i}번째 : {a[i]}")
    print(f"Big_num : {big_num}")
    return big_num
    
a = [1, 2, 3, 4, 5]
find_biggest_num(a)