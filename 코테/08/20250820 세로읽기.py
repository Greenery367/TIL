arr = []

for i in range(5):
    arr.append(list(input().split()))


for j in range(0, 15):
    for k in range(0, 5):
        if len(arr[k][0])-1 >= j:
            print(arr[k][0][j], end="")
        else: pass