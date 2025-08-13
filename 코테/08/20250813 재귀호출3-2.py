def repeat(x):
    if x == 6:
        return
    print(x, end = " ")
    repeat(x+1)
    print(x, end = " ")
repeat(0)