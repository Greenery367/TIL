T = int(input())

def check_candys(arr):
    # 조건 미충족 => -1
    if arr[2] <= 2 or arr[1] <= 1 or arr.count(0) > 0 :
        return -1

    # 조건 충족 => 0
    elif arr[0] < arr[1] < arr[2]:
        return 0

    # 검사
    else:
        count = 0
        if arr[1] >= arr[2] :
            var1 = arr[1] - arr[2] + 1
            arr[1] -= var1
            count += var1
        if arr[0] >= arr[1]:
            var2 = arr[0] - arr[1] + 1
            arr[0] -= var2
            count += var2
        return count

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f"#{tc} {check_candys(arr)}")