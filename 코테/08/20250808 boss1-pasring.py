T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = ""

    # 가로에서 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            sub = arr[i][j:j + M]
            if sub == sub[::-1]:
                result = sub
                break
        if result:
            break

    # 세로에서 회문 찾기 (가로에서 못 찾았을 때만)
    if not result:
        for i in range(N - M + 1):
            for j in range(N):
                sub = ''.join(arr[k][j] for k in range(i, i + M))
                if sub == sub[::-1]:
                    result = sub
                    break
            if result:
                break

    print(f"#{tc} {result}")
