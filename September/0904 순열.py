path = []
# used[] : 고를 수 있는 수만큼 만들기
used = [False, False,  False, False,False, False, False]
# used =[False] * N : N개의 카드 종류가 있는 경우
# used = [False] * 7 (1~6)

def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in range(1,7):
        continue

    used[num] = 1
    path.append(num)
    recur(cnt+1)
    path.pop()
    used[num] = 0