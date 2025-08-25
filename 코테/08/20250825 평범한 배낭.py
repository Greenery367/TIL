N, K = map(int,input().split())
arr = []
for n in range(N):
    arr.append(tuple(map(int, input().split())))
sorted_arr = sorted(arr, key=lambda x: (x[0], x[1]))
current = 0
result = 0

for i in sorted_arr:
    if current + i[0] > K:
        print(result)
        break

    current += i[0]
    result += i[1]
