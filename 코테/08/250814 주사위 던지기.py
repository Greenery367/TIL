def dice_combinations(n, start=1, path=[]):
    if n == 0:
        print(' '.join(map(str, path)))
        return

    for i in range(start, 7):  # 1~6까지, start 이상부터 (비내림차순)
        dice_combinations(n - 1, i, path + [i])


# 입력
N = int(input())
dice_combinations(N)
