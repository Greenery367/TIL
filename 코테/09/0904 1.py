arr= [0 for i in range(4)]
arr[0] = [1,3]
arr[1] = [2]
arr[2] = [0,3]
arr[3] = [2]

used = [False for j in range(4)]
#그래프는 사이클때문에 탐색할 때 무한 loop
def recur(now):
    print(now)
    for i in range(len(arr[now])):
        next = arr[now][i]
        used[now] = True
        if used[next] == False:
            recur(next)
        else: pass
    return

recur(0)
