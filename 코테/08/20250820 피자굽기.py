T = int(input())

for i in range(1,T+1):
    N,M = map(int, input().split())
    pizza_arr = list(map(int, input().split()))

    # 오븐에 피자 넣기
    turn = 1
    oven = []
    for n in range(N):
        oven.append(pizza_arr[0])
        pizza_arr.pop(0)


    while True:
        print(turn)
        print(pizza_arr)
        print(oven)

        if len(oven) == 1 :
            break

        if turn == N:
            turn = 1
            for s in range(len(oven)):
                oven[s] = oven[s] // 2

        if oven[0] == 0:
            oven.pop(0)
            oven.append(pizza_arr[0])
        else :
            a = oven.pop(0)
            oven.append(a)

        turn += 1

    print(f"#{tc} {oven[0]}")