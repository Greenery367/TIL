structures = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    map1 = [list(map(int, input().split())) for _ in range(N)]
    start = [R, C]

    # 파이프가 있는지 없는지 체크크