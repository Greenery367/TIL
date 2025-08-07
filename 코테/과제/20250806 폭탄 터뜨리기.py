N, M = map(int, input().split())
K = int(input())

situation = []
bomb_list = []
for i in range(N):
    situation.append(list(map(str, list(input()))))
    
# 폭탄 위치 찾기
for j in range(0, N):
    for k in range(0, M):
        if situation[j][k] == "@":
            situation[j][k] = "%"
            bomb_list.append([j, k])

# 위치 배열
dy = [-1, 0, 0, +1]
dx = [0, -1, +1, 0]


for f in range(len(bomb_list)):
    for kk in range(1, K+1):
        for h in range(len(dy)):
            bomb = bomb_list[f]
            ny = bomb[0] + dy[h] * kk
            nx = bomb[1] + dx[h] * kk
        
            if N > ny > -1 and M > nx > -1 and situation[ny][nx] == "_":
                if (situation[ny][nx+1] == "#" or situation[ny][nx-1] == "#") or (situation[ny-1][nx] == "#" or situation[ny+1][nx] == "#"):
                    break
                else :
                    situation[ny][nx] = "%"
            
for ii in situation :
    print(*ii)