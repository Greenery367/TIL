# 가장 작은 두 수를 선택하기(내림차순)
# 더한 값을 배열에 다시 넣고(append) 정렬
# 모든 수가 하나로 합쳐질 때 까지 반복

N = int(input())
arr = list(map(int, input().split()))

sum_v = 0
# 내림차순 정렬
arr.sort(reverse = True)

while len(arr) > 1:
    temp = arr.pop() + arr.pop()
    sum_v += temp

    arr.append(temp) # append() 넣기
    arr.sort(reverse = True) # sort(reverse = True) 정렬하기

print(sum_v)