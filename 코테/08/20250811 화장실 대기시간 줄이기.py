arr = list(map(int, input().split()))
num = len(arr)

arr.sort()

print(arr[0]*3 + arr[1]*2+ arr[2]*1)