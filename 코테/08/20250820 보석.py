N,M,T,K = map(int, input().split())
map_arr = [[0]*N for m in range(M)]
for i in range(T):
    x,y = map(int, input().split())
    map_arr[y-1][x-1] = 1

print(map_arr)

max_v = -1
result = []
for j in range(K, M-K+1):
    for k in range(K, N-K+1):
        total = 0
        for f in range(K):
            total += map_arr[j+f][k:k+4].count(1)
        if total > max_v:
            result = [j,k]

print(*result)
print(max_v)