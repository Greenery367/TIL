arr = [
    [1,2,1,3,1],
    [2,2,2,2,2,],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

y = 1
x = 2
sum_v = 0

# sum_v += arr[i-1][j]
# sum_v += arr[i+1][j]
# sum_v += arr[i][j-1]
# sum_v += arr[i][j+1]

# print(sum_v)

# 상하좌우 방향배열 자료구조
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 방향이 네 방향이라서 4번 반복한다.
for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    sum_v = arr[ny][nx]
    
print(sum_v)