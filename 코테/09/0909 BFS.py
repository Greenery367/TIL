from collections import deque

lst = [[
    [0,1,1,0,0],
    [1,0,1,0,0],
    [1,1,0,1,0],
    [0,0,1,0,1],
    [0,0,0,1,0]
]]
txt ='ABCDE'

visited = [False] * 5
q = deque()
var = int(input())
q.append(var)
visited[var] = True

while q:
    now = q.popleft()
    print(txt[now], end=' ')

    for i in lst[now]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
        else: pass