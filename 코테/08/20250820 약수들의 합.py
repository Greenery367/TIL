while True:
    a = int(input())
    arr = []

    if a == -1 : break
    else :
        for i in range(1, a):
            if a % i == 0 : arr.append(i)
            else : pass

        if sum(arr) != a :
            print(f"{a} is NOT perfect.")
        else :
            arr.sort()
            print(f"{a} = ", end="")
            for j in arr :
                if j != arr[-1] : print(f"{j} + ", end = "")
                else : print(f"{j}")