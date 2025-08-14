arr = ['A', 'B', 'C', 'D', 'E']

for a in range(5):
    start1 = a + 1
    for b in range(start1, 5): # a에서 뽑은건 포함하면 안 된다
        start2 = b + 1
        for c in range(start2, 5): # b에서 뽑은건 포함하면 안 된다
            print(arr[a], arr[b], arr[c])

######################

arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3

def KFC(lev, start):
    if lev == n : # level = 3
        print(*path)
        return

    for i in range(start, 5): # branch는 최대 5
        path.append(arr[i])
        KFC(lev + 1, i+1)
        path.pop()

KFC(0,0)