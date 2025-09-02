arr = [None]*3
arr[0] = ['A', 'B', 'T']
arr[1] = []
arr[2] = ['R','S']

for i in range(3):
    for j in range(len(arr[i])): print(arr[i].pop(-1), end="")
    print()