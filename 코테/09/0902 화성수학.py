T = int(input())
for _ in range(T):
    arr = list(input().split())
    result = float(arr[0])  # 초기값은 숫자로 변환
    for i in range(1, len(arr)):
        if arr[i] == '@':
            result *= 3
        elif arr[i] == '%':
            result += 5
        elif arr[i] == '#':
            result -= 7

    print(f"{result:.2f}")  # 소수점 둘째 자리까지 출력
