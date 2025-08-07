arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

x,y = map(int, input().split())

max_v = 0

dy = [0,0,-1,-1]
dx = [-1,+1,0,+1]

for i in range(4) :
    ny = y + dy[i]
    nx = x + dx[i]
    
    if max_v < arr[ny][nx] :
        max_v = arr[ny][nx]
        
print(max_v)