N, S = map(int, input().split())
arr = list(map(int, input().split()))
path = []
lst =[]

def dfs(cnt, subset):
    if cnt == len(arr):
        lst.append(subset)
        print(*subset)
        return

    dfs(cnt+1, subset+[arr[cnt]])
    dfs(cnt+1, subset)

dfs(0,[])

count = 0
for i in lst :
    if sum(i) == S and i != []:
        count += 1
print(count)