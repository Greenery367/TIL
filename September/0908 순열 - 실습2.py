path = []
used = [] * 3

def recur(lev):
    if lev == 2:
        print(path)
        return

    for i in range(3):
        if used[i] == 1 : continue;
        used[i] = 1
        path.append(i)
        recur(lev+1)
        path.pop()
        used[i] = 0