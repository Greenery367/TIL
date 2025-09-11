arr = ['O', 'X']
path = []
name = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def recur(lev):
    sum_v = 0
    # 현재까지 합계 계산
    for i in range(len(path)):
        if path[i] == 'O':
            sum_v += name[i]

    # 가지치기 (시간복잡도상 효율적)
    if sum_v > 10: return

    if lev == 10: # level : 10
        if sum_v == 10:
            # 정점 레벨에 도달했을 때 출력
            for i in range(len(path)):
                if path[i] == 'O':
                    print(name[i], end = ' ')
            print()
        return

    for i in range(2): # branch : 2
        path.append(arr[i])
        recur(lev + 1)
        path.pop()

recur(0)