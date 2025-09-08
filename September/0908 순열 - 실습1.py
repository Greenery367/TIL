path = []

def recur(lev):
    if lev == 2:
        print(path)
        return

    for i in range(3):
        path.append(i)
        recur(lev+1)
        path.pop()