
n,m= map(int, input().split())
arr = list(map(int, input().split()))

gap = n - m + 1
max_v = -1
idx = -3

for i in range(gap):
    sum1 = sum(arr[i:i+m])
    if sum1 > max_v:
        max_v = sum1
        idx = i
print(idx)