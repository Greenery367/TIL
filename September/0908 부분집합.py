arr = ['O','X']
name = ['MIN', 'CO', 'TIM']
path = []

def recur(cnt):
    # 종료 조건 (3명을 모두 고려)
    if cnt == 3 :
        print(*path)
        return

    # 재귀호출 파트
    # 부분집합에 포함되는 경우 (0을 추가)
    path.append(arr[0])
    recur(cnt+1)
    path.pop()

    # 부분집합에 포함되지 않는 경우 (X를 추가)
    path.append(arr[1])
    recur(cnt+1)
    path.pop()

# 0명을 고려한 상태로 시작
recur(0)

