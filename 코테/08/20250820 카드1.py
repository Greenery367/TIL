N = int(input())
arr = [i for i in range(1,N+1)]
result = []

while True:
    if len(arr) == 0 :
        break
    elif len(arr) == 1 :
        result.append(arr[0])
        break
    elif len(arr) == 2 :
        result.append(arr.pop(0))
        result.append(arr.pop(0))
    else:
        result.append(arr.pop(0))
        a = arr.pop(0)
        arr.append(a)

print(*result)