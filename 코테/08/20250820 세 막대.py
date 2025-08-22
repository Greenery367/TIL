arr = list(map(int, input().split()))
arr.sort()

if arr[2] >= arr[1] + arr[0]:
    arr[2] = arr[1]+arr[0]-1

print(sum(arr))