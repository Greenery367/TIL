

# 5x5 행렬
visited = [[0] * 5 for i in range(5)]

# 방향 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def flood_fill(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    visited[start_y][start_x] = 1
x,y = map(int, input().split())

