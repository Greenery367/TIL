N, M = map(int, input().split())
arr = [input() for n in range(N)]
answer = [input() for m in range(M)]
for i in range(M):
    if answer[i].isdecimal(): print(arr[int(answer[i])-1])
    else: print(arr.index(answer[i])+1)