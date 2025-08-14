path = []
used = [0] * 7

def KFC(lev):

    if lev ==4:
        print(*path)
        return

    for i in range(1, 7):
        # 만약 used[]에 기록되어 있으면 재귀호출 하지 않는다.
        # -> 다음 레벨로 탐색하지 않는다.
        if used[i] == 1 : continue

        # 만약 used[i]에 없으면 계속 탐색
        used[i] = 1 # 기록
        path.append(i)
        KFC(lev + 1)
        path.pop()
        used[i] = 0

KFC(1)