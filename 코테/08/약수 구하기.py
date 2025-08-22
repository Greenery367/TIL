a, b = map(int, input().split())
arr = []
for i in range(1, a+1):
    if a % i == 0 :
        arr.append(i)

if len(arr) >= b :
    print(arr[b-1])
else :
    print(0)