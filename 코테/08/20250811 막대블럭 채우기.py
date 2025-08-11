n = int(input())
block_arr = list(map(int, input().split()))
block_arr.sort()

total = 100
result = 0
for i in range(n):
    if total >= block_arr[i] :
        total -= block_arr[i]
        result += 1
    else :
        print(result)
        break