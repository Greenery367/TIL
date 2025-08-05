arr = [12, 3, 9, 1, 15, 7]
num = len(arr)

for i in range(num):
    for j in range(num-1):
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
    
print(*arr)