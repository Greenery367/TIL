

m = [[] for _ in range(3)]

m[0] = ['A','B','T']
m[2] = ['R', 'S']

for y in range(len(m)):
    for x in range(len(m[y])-1, -1, -1):
        print(m[y][x], end= '')
    print()