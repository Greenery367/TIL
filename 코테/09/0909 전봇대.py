T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[0])
    lst = [0]*10001

    for i in arr:
        var = abs(i[0]-i[1])
        if var == 0:
            lst[i[0]] += 1
        for v in range(var):
            lst[v+1] += 1
    if max(lst) > 1:
        count = 0
        for i in lst:
            if i > 1: count += 1
        print(f"#{tc} {count}")
    else: print(f"#{tc} 0")