T = int(input())

for k in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    current = 1
    biggest = 1

    for i in range(1, N):
        if arr[i] == arr[i-1] and arr[i] == 1:
            current += 1
        else:
            biggest = max(biggest, current)
            current = 1

    biggest = max(biggest, current)  # 마지막 연속 처리
    print(f"#{k} {biggest}")
