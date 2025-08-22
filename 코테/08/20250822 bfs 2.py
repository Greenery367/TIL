from collections import deque

# 인접 행렬 초기화 (7x7)
adj = [[0] * 7 for _ in range(7)]

# 노드 간 연결 설정 (이미지 기준)
adj[0][1] = 1  # A -> C
adj[0][2] = 1  # A -> B
adj[0][3] = 1  # A -> Q

adj[2][4] = 1  # B -> T
adj[2][5] = 1  # B -> P

adj[3][5] = 1  # Q -> P
adj[3][6] = 1  # Q -> R

# BFS 탐색 준비
visited = [False] * 7
q = deque()
q.append(0)  # A부터 시작
visited[0] = True

# 노드 이름 리스트
name = ['A', 'C', 'B', 'Q', 'T', 'P', 'R']

# BFS 수행
while q:
    now = q.popleft()
    print(name[now], end=' ')

    for i in range(7):
        if adj[now][i] == 1 and not visited[i]:
            visited[i] = True
            q.append(i)
