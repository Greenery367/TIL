T = int(input())

for tc in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(input().split()))
    arr.sort(key =lambda x:int(x[1]))
    print(arr[-1][0])