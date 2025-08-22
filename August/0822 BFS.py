map = [[0] * 7 for i in range(7)]
map[0][1] = 1
map[0][1] = 1
map[2][4] = 1
map[4][5] = 1
map[4][6] = 1

alist = list([] for _ in range(7))
alist[0] = [1, 2]
alist[1] = [3]
alist[2] = [4]
alist[4] = [5,6]
print(alist)


q = deque()
q.append(0) # 시작 지점

name = "ABCDEFG"

while q:
    # 1. 큐에서 뺀다(탐색)
    now = q[0] # now는 탐색하고 있는 현재 노드
    q.popleft()
    print(name[now], end=' ')

    # 2. 다음 갈 곳 예약 걸기 (큐 등록)
    for i in range(len(alist[now]))