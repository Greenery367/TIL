arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

x,y = map(int, input().split())

dy=[-1,0,-1,+1,+1]
dx=[-1,0,+1,-1,+1]

total = 1

for i in range(5):
    ny = y+dy[i]
    nx = x+dx[i]
    total *= arr[ny][nx]

print(total)