path = []

def dice(lev, limit):

    if lev == limit+1:
        if path[0] != path[1]: print(*path)
        return

    for i in range(1,7):
        path.append(i)
        dice(lev+1, limit)
        path.pop()

dice(1, int(input()))