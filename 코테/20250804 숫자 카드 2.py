# N : 상근이가 가진 숫자 카드의 개수
N = int(input())
# 상근이가 가진 숫자 카드들
arr = list(map(int, input().split()))
# M : 상근이가 몇 개 가지고 있는지 찾아야 할 개수 M
M = int(input())
# 상근이가 몇 개 가지고 있는지 찾아야 할 정수들
arr_m = list(map(int, input().split()))

# 결과로 출력할 배열
result_arr = []

for i in arr_m:
    a = arr.count(i)
    result_arr