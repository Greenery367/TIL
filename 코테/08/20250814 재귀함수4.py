def KFC(x):
    if x == 3:
        return
    for i in range(2):
        KFC(x+1)
    print(x)
KFC(0)