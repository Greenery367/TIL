# 1. 가변
# 2. 시퀀스
# 가변 시퀀스 -> 알고리즘에 많이 쓰임 (모든게 리스트)
arr = [1, 2, 3, [4, 5, 6]]
print(arr[3][0])
print(arr[3][:])
print(arr[3][::-1])

# len 함수
print(len(arr))