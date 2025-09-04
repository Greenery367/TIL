arr = [[0,0,0,0,0,0] for i in range(6)]
arr[0] = [0,1,1,1,0,0]
arr[1] = [0,0,0,0,1,1]

tree = 'ABTQVX'

lst = arr[int(input())]
for i in range(6) :
    if lst[i] == 1 : print(tree[i])
