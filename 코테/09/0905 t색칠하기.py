T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    grid = [[0] * 10 for i in range(10)]
    count = 0
    for m in range(n):
        for a in range(lst[m][0], lst[m][2]+1):
            for b in range(lst[m][1], lst[m][3]+1):
                if grid[a][b] != '#' and grid[a][b] != 0:
                    grid[a][b] = '#'
                    count += 1
                elif grid[a][b] == 0:
                    grid[a][b] = lst[m][4]
                else:
                    continue
    print(f"#{tc} {count}")
