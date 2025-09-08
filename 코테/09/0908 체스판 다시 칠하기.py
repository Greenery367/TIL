N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_count = 64  # 최대 64칸 전부 다시 칠하는 경우

for i in range(N - 7):  # 세로 시작점
    for j in range(M - 7):  # 가로 시작점
        w_start = 0  # 좌상단이 W인 경우 다시 칠해야 할 수
        b_start = 0  # 좌상단이 B인 경우 다시 칠해야 할 수

        for x in range(8):
            for y in range(8):
                # 현재 위치의 실제 색
                current = board[i + x][j + y]

                # 체스판 패턴상 기대되는 색 (x+y가 짝수면 좌상단과 같아야 함)
                if (x + y) % 2 == 0:
                    if current != 'W': w_start += 1
                    if current != 'B': b_start += 1
                else:
                    if current != 'B': w_start += 1
                    if current != 'W': b_start += 1

        min_count = min(min_count, w_start, b_start)

print(min_count)
