arr = input().split()
n = len(arr)
result = 0
def get_num(tar):
    count = 0
    for i in range(n) :
        if tar & 0x1:
            count += 1
        tar >>= 1
    return count

for tar in range(1 << n):
    if get_num(tar) >= 2 : # 비트가 2개 이상 1이라면
        result += 1
print(result)
