used = [0] * 6
path = []
is_babygin = 0

def is_baby_gin():
    cnt = 0
    # 앞에 세자리가 triplet 또는 run
    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif (a) == (b - 1) == (c - 2) : cnt += 1

    # 뒤에 세자리가 triplet 또는 run
    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif (a) == (b - 1) == (c - 2) : cnt += 1

    return cnt == 2 # cnt 가 2면 baby-gin이 맞다!

# 순열 코드
def recur(lev):
    global is_babygin
    if lev == 6: # level은 6
        if is_baby_gin():
            is_babygin = 1
        return

    for i in range(6): # branch는 6
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        recur(lev + 1)
        path.pop()
        used[i] = 0

arr = list(map(int, input().split()))
recur(0)

if is_babygin: print('Yes')
else: print('No')
