N, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : x[1])
end_time = [0] * K
count = 0

for i in range(N):
    for j in range(K):
        if end_time[j] <= arr[i][0]:
            end_time[j] = arr[i][1]
            count += 1
        else : continue

print(count)