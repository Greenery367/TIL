N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for n in range(N)]
arr = sorted(arr, key=lambda x:(x[0], x[1]))

weight = 0
result = 0
for n in range(N):
    if weight + arr[n][0] <= K :
        weight+= arr[n][0]
        result += arr[n][1]
    else: continue
print(result)