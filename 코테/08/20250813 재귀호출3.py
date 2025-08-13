def repeat(flag, N):
    if flag == True and N == -1:
        return

    if flag == False and N < 5 :
        print(N)
        N += 1
    elif flag == False and N == 5 :
        flag = True
        for i in range(2) : print(N) 
        N -= 1
    elif flag == True and N > -1 :
        print(N)
        N -= 1

    repeat(flag, N)

flag = False
N = 0

repeat(flag, N)