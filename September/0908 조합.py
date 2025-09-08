arr = ['A','B','C','D','E']

# 1. 반복문 구현
for a in range(5):
    start1 = a+1
    for b in range(start1, 5):
        start2 = start1 + 1
        for c in range(start2, 5):
            start3 = start2 + 1
            print(a,b,c)

# 2. 함수로 구현하기
def recur(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        recur(lev+1, i+1)
        path.pop()