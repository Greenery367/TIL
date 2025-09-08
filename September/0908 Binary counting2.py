arr = [1, 2, 3, 4]
n = len(arr)  # 꼭 필요함!

def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(n):
        if tar & 0x1:  # 가장 오른쪽 비트가 1이면
            print(arr[i], end='')
        tar >>= 1  # 비트를 오른쪽으로 한 칸 민다 (다음 자리 체크)

for target in range(1 << n):  # 0 ~ 15
    get_sub(target)
    print()
