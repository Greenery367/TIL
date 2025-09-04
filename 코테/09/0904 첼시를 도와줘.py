T = int(input())

for tc in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(input().split())
    arr.sort(key = lambda x: int(x[0]))
    print(arr[-1][1])