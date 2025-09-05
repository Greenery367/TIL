def binary_search(target, total):
    left = 1
    right = total
    count = 0

    while left <= right:
        count += 1
        mid = (left + right) // 2

        if mid == target:
            return count
        elif mid > target:
            right = mid
        else:
            left = mid

T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    a_count = binary_search(Pa, P)
    b_count = binary_search(Pb, P)

    if a_count < b_count:
        result = "A"
    elif a_count > b_count:
        result = "B"
    else:
        result = "0"

    print(f"#{tc} {result}")
