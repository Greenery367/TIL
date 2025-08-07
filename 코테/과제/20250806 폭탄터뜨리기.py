def bomb(arr):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    for y in range(N):
        for x in range(M):
            if arr[y][x] == '@': # 폭탄 발견 하면 터뜨리기
                for i in range(4): # 4방향으로
                    for k in range(1, K + 1): # K만큼
                        ny, nx = y + k * dy[i], x + k * dx[i]
                        if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
                        if arr[ny][nx] == '_': arr[ny][nx] = '%' # 폭탄이 터진다
                        elif arr[ny][nx] == '#': break # 벽만 나면 break
                arr[y][x] = '%' # 현재위치에서 폭탄 터지기


N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]

bomb(arr)

for row in arr:
    print(*row, sep='')