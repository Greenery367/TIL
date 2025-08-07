def get_sum(y, x):
    dy = [-1, 1, 0, 0] # 4방향(상하좌우)
    dx = [0, 0, -1, 1]
    sum_v = arr[y][x] # 초기화 (핵심 : 한번만 더하기)
    for i in range(4):
        for k in range(1, P+1):
            ny, nx = y + dy[i] * k, x + dx[i] * k
            if ny < 0 or ny >= N or nx < 0 or nx >= N : continue
            

T = int(input())

for tx in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            result = max()
            
            