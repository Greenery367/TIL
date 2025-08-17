T = int(input())
for i in range(T):
    K,N,M = map(int, input().split())
    station_arr = list(map(int, input().split()))
    
    result = 0
    start = K
    for j in range(M):
        far = start + K
        for k in range(M):
            
    print(result)