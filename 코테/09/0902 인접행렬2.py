inp = int(input())

arr = [
    [0,1,0,0,0],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0]
]

lst = arr[inp-1]

for i in range(5):
    if lst[i] == 1:
        print(i+1)
