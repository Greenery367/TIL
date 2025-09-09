import sys
sys.stdin = open("input.txt", "r")

# 1. BFS로 접근
# - 이동 방향: 상하좌우
# - 이동이 불가능한 케이스
#  - [델타 배열 기본] 범위 밖으로 나가면 못감
#  - [방문 기록 기본] 이미 방문한 곳은 못감
#  - [문제 조건]
#   - 현재 내 위치에서 뚫려있는 곳만 이동 가능
#   - 현재 내 위치에서 뚫려있는 곳만 이동 가능
# 2. 방문 기록을 해야 한다. (visited)

# 델타 배열
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 터널들의 종류에 따라 이동가능 여부를 기록
types = {
    1: [1,1,1,1],
    2: [1,1,0,0],
    3: [0,0,1,1],
    4: [1,0,0,1],
    5: [0,1,0,1],
    6: [0,1,1,0],
    7: [1,0,1,0]
}

def bfs(R,C):
    q = [(R,C)] # 후보군
    visited[R][C] = 1

    while q:

        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:

            next_dirs = types


T = int(input())

for tc in range(1, T+1):
    N,M,R,C,L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 특정 좌표까지 몇 시간이 걸렸는지 기록
    visited = [[0] * M for _ in range(N)]

    bfs(R,C)
