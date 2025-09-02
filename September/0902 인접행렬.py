ask = int(input())

arr = [
    [0,0,0,0],
    [1,0,0,0],
    [1,1,0,0],
    [1,1,0,0]
]
lst = ['B','T','A','R']

for i in range(4):
    if arr[ask][i] == 1:
        print(lst[i])