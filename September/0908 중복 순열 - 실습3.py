arr = ['A','B','C']
n = len(arr)

# 1. 함수로 해결
def get_sum(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end=' ')
        tar >>= 1

# 2. 반복해서 호출
for tar in range(1 << n): #모든 경우는 n의 제곱
    get_sum(tar)
    print()