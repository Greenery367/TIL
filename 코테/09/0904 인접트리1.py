tree = [[0] * 6 for i in range(6)]

tree[0][1] = 1
tree[0][2] = 1
tree[0][3] = 1

tree[1][4] = 1
tree[1][5] = 1

def search_tree(now):
    print(now, end=' ')
    for i in range(6):
        if tree[now][i] == 0 : continue
        search_tree(i)

search_tree(0)