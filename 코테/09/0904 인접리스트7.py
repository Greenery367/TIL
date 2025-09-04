arr = [[] for i in range(5)]
arr[0] = ['U','R','K']
arr[1] = ['S','R']
arr[3] = ['S','K']
arr[4] = ['R', 'U']

var = int(input())
lst = arr[var]
for i in lst : print(i)