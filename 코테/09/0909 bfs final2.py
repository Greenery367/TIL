from collections import deque

MAP = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

q = deque()
used = [0] * 5
start, end = map(int, input().split())
# start 노드 q에 넣어주고,
# level도 같이 넣어준다. q.append((node, level))
q.append((start, 0))
used[start] = 1 # 시작노드 방문처리

while q:
    # 1. 큐에서 뺀다(탐색)
    now, level = q[0]
    q.popleft()

    # now가 end에 도착했을때 break
    if now == end:
        print(level) # 비행기를 몇번 탔는지
        break

    # 2. 다음 갈곳 예약 걸기(큐에 등록)
    for i in range(5):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        q.append((i, level + 1)) # 큐 등록