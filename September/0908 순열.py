# 5명 중 3명을 순서 없이 고르기
arr = ['A','B','C','D','E']
n = 3
path = []

def recur(cnt, start):
    # N명을 뽑으면 종료
    if cnt == n:
        print(*path)
        return
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i+1) # i번째를 골랐으니, 다음 선택은 i+1부터 고려
        # recur(cnt+1, i) # 중복조합
        path.pop()

recur(0,0)