arr = [list(map(int, input().split())) for _ in range(4)]

for y in range(3, -1, -1): # 3부터 0까지 1씩 감소
    for x in range(3, -1, -1): # 3부터 0까지 1씩 감소
        print(arr[y][x], end = ' ')
    print() # 줄바꿈