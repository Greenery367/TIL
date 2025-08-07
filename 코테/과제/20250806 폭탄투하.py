# 4x5 배열 만들기
arr = [["_"]*5 for _ in range(5)]

# 폭탄1이 떨어지는 장소
x,y = map(int, input().split())
# 폭탄2이 떨어지는 장소
x1,y1 = map(int, input().split())
x_arr = [x, x1]
y_arr = [y, y1]

#폭탄 투하 후 터지는 장소들의 좌표
dx = [-1,0,+1,-1,+1,-1,0,+1]
dy = [-1,-1,-1,0,0,+1,+1,+1]

for i in range(2):
    for j in range(len(dx)):
        ny = y_arr[i]+dy[j]
        nx = x_arr[i]+dx[j]
        if 4 >= ny > -1 and 4 >= nx > -1 :
            arr[ny][nx] = "#"
        
for i in range(len(arr)):
    print(*arr[i])