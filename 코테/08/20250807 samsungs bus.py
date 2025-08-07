T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 버스 노선 수
    station_array = [0] * 5001  # 정류장 1~5000까지

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            station_array[i] += 1

    P = int(input())  # 질의 수
    result = []

    for _ in range(P):
        Cj = int(input())  # 질의 정류장 번호
        result.append(station_array[Cj])

    print(f"#{tc}", *result)
