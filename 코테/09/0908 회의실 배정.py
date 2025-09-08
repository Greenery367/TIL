N = int(input())
arr = []

for n in range(N): arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[1], x[1]-x[0]))

result = 0
current = 0

for i in range(len(arr)):
    if current <= arr[i][0]:
        current = arr[i][1]
        result += 1
    else: continue

print(result)