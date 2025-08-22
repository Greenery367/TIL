N = int(input())
M = int(input())
arr = []
for i in range(N, M+1):
    flag = True
    if i <= 1 : continue
    for j in range(2, i):
        if i % j == 0 :
            flag = False
            break
    if flag == True:
        arr.append(i)
    else :
        flag = False

if len(arr) > 0 :
    print(sum(arr))
    print(arr[0])
else :
    print(-1)