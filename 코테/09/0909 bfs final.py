from collections import deque

def bfs(start, end):
    q = deque()
    used = [0] * 5
    q.append(start)
    used[start] = 1

    count = 0
    while q:
        now = q.popleft()

        if now == end:
            print(count)
            return
        for i in lst[now]:
            if not used[i]:
                used[i] = True
                count += 1
                q.append(i)

lst = [[] for _ in range(5)]
lst[0] = [1,4]
lst[1] = [3,4]
lst[2] = [0]
lst[3] = [0,2]

start, end = map(int, input().split())
bfs(start, end)

