MAP = [
    [0,1,1,1,0,0],
    [1,0,1,1,0,0],
    [1,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,1,0,0,1],
    [0,0,0,0,0,0]
]

def dfs(now):
    print(now, end=" ")
    for i in range(6):
        if MAP[now][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False

visited = [False] * 6
visited[4] = True
dfs(4)