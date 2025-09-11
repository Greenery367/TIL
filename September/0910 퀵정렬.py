T = int(input())

def quick_sort(arr):
    if len(arr) <= 1 : return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    result = quick_sort(left) + middle + quick_sort(right)
    return result

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick_sort(arr)
    print(f"#{tc} {result[len(result) // 2]}")