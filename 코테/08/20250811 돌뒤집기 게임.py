T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone_arr = list(map(int, input().split()))

    order_arr = []
    for a in range(M): order_arr.append(list(map(int, input().split())))

    for i in range(len(order_arr)):
        for j in range(1, J + 1):
            I = order_arr[i][0]
            if I - j - 1 < 0:
                break
            if I - j > -1 and I + j < N:
                if stone_arr[I - j - 1] == stone_arr[I + j - 1] and stone_arr[I - j - 1] == 1:
                    stone_arr[I - j - 1] = 0
                    stone_arr[I + j - 1] = 0
                elif stone_arr[I - j - 1] == stone_arr[I + j - 1] and stone_arr[I - j - 1] == 0:
                    stone_arr[I - j - 1] = 1
                    stone_arr[I + j - 1] = 1
                else:
                    pass
            else:
                break

    print(f"#{tc} {stone_arr}")