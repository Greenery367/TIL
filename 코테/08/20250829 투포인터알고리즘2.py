n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
current_sum = 0
result = 0

while True:
    if current_sum >= m:
        print(f"start 줄임: {arr[start]} 빼기 -> 합: {current_sum} -> ", end="")
        current_sum -= arr[start]
        start += 1
        print(f"{current_sum}")
    elif end == n:
        break
    else:
        print(f"end 늘림: {arr[end]} 더하기 -> 합: {current_sum} -> ", end="")
        current_sum += arr[end]
        end += 1
        print(f"{current_sum}")

    if current_sum == m:
        print(f"✅ 구간 발견! start={start}, end={end-1}, 합={current_sum}")
        result += 1
