def print_recursive(N, var):
    if var == N*1000 + N*100 + N*10 + N:  # 종료 조건: 3333 도달 시 종료 (예: N=3)
        return

    if var % 1000 < N:
        var += 1
        print(var)

    elif var % 1000 == N:
        var += 101 - N
        print(var)  # ← 여기 세미콜론 아닌 `'` 오타 있음

    return print_recursive(N, var)

print_recursive(3, 1111)
