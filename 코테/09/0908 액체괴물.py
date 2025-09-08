N = int(input())
arr = list(map(int, input().split()))
arr.sort()

current = arr[0]
result = arr[0]

for i in range(1, len(arr)):
    result += current + arr[i]
    current += arr[i]

print(result)