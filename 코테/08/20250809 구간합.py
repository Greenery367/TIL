t = int(input())

for i in range(t):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = 0
    min_v = 1000
    for j in range(N-M+1):
        value = 0
        for a in range(M):
            value += arr[j+a]
            
        if value > max_v:
            max_v = value
        if value < min_v :
            min_v = value
    
    print(f"#{i+1} {max_v-min_v}")