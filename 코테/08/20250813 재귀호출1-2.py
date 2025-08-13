def print4(N, var):
    if var == (N*10)+N :
        print(str(var)[0],str(var)[1])
        return

    if var%10 < N :
        print(str(var)[0],str(var)[1])
        var = var + 1

    elif var%10 == N:
        print(str(var)[0],str(var)[1])
        var += 11-N

    return print4(N, var)

print4(3, 11)