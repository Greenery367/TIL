arr = ['O','X']
name = ['MIN', 'CO', 'TIM']
path = []

# 두번째 선택에서는
# 'MIN'이라는 친구가 포함된 상태로 넘겨줄 수 있지 않을까
def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return

    # 부분집합에 포함시키는 경우
    recur(cnt+1, subset+[name[cnt]])
    # 부분집합에 포함시키지 않는 경우
    recur(cnt + 1, subset)

recur(0,[])