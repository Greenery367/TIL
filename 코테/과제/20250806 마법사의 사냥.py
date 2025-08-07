N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

K = int(input())

# Directions: top-left, top-right, bottom-left, bottom-right
dy = [-1, -1, 1, 1]
dx = [-1, 1, -1, 1]

max_kill = 0

for i in range(N):
    for j in range(N):
        total = 0
        for d in range(4):
            for step in range(1, K + 1):
                ny = i + dy[d] * step
                nx = j + dx[d] * step
                if 0 <= ny < N and 0 <= nx < N:
                    total += field[ny][nx]
        if total > max_kill:
            max_kill = total

print(max_kill)
