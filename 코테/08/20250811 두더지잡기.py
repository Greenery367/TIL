T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    moll_arr = []

    for n in range(N):
        moll_arr.append(list(input()))

    biggest = 0

    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(M):
                for f in range(M):
                    ny = i + k
                    nx = j + f

                    if moll_arr[ny][nx] == '@':
                        total += 1

        if total > biggest :
            biggest = total

    print(f"#{tc} {biggest}")