n = int(input())
path = []
sum_v = 0

def KFC(level):
    global sum_v

    if level == n:
        print(sum_v)
        return

    for i in range(1,7):
        if sum(path) > 10 : return

        path.append(i)
        sum_v += sum(path)
        KFC(level+1)
        path.pop()

KFC(0)