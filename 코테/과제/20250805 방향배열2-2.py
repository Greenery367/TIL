arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

x = 1
y = 0

dy = [0,+1,0]
dx = [-1,0,+1]

sum_v = 0

for i in range(3):
    nx = x + dx[i]
    ny = y + dy[i]
    sum_v += arr[ny][nx]
    
print(sum_v)