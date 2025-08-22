T = int(input())
arr = [[0]*100 for tc in range(100)]
count1 = 0
doubled = 0

a = [list(map(int,input().split())) for tc in range(T)]

for i in range(len(a)):
    x = a[i][0]
    y = a[i][1]

    for j in range(x, x+10):
        for k in range(y, y+10):
            if arr[j][k] == 0 :
                arr[j][k] = 1
                count1 += 1
                pass
            elif arr[j][k] == 1 :
                arr[j][k] = 2
                doubled += 1
print(count1)