T = int(input())

for i in range(1, T + 1):
    N, P = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]    
    best_result = 0
    
    dy = [-1, 0, 0, +1]
    dx = [0, -1, +1, 0]
    
    for j in range(N):
        for k in range(N):
            total = town[j][k]
            # 폭탄의 위력만큼
            for var in range(4):
                for f in range(1, P+1):
                # 여러 방향으로
                    # total += town[j][k] # 4번 더해진다.
                    ny = j + dy[var] * f
                    nx = k + dx[var] * f
                    
                    if not (-1 < ny < N and -1 < nx < N): continue
                    total += town[ny][nx]
                    
            if total > best_result :
                best_result = total
            
    
    print(f"#{i} {best_result}")