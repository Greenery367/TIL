
N = int(input())
arr = list(map(int, input().split()))
current = 1
result = 0

while True:
    if current == N :
        break

    if current == 1 or arr[current-1] == 0:
        current += 1
        result += 1

    else :
        if arr[current-1] != current :
            temp = current
            current = arr[current-1]
            arr[temp - 1] = 0
            result += 1
print(f"#{tc} {result}")
