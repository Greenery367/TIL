# 가장 작은 두 수를 선택하기(내림차순)
# 더한 값을 배열에 다시 넣고(append) 정렬
# 모든 수가 하나로 합쳐질 때 까지 반복

T = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

total_time = 0

for t in range(T):
    if len(arr) == 0:
        break

    elif len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        total_time += a+b
        arr.append(total_time)
        arr.sort(reverse=True)

    elif len(arr) == 1:
        total_time += arr.pop()
        break


print(total_time)