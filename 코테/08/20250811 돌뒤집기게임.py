T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    dol_arr = list(map(int, input().split()))
    address = [list(map(int, input().split())) for M in range(M)]

    for m in range(M):
        i = address[m][0]
        j = address[m][1]
        for f in range(j):
            if i-j > -1 and i+j < len(dol_arr)-1 :
                if dol_arr[i - f] == dol_arr[i + f] and dol_arr[i-f] == 0 :
                    dol_arr[i - f], dol_arr[i + f] = 1
                elif dol_arr[i - f] == dol_arr[i + f] and dol_arr[i-f] == 1 :
                    dol_arr[i - f], dol_arr[i + f] = 0


    print(dol_arr)