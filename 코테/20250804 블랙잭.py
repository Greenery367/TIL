# N : 카드의 개수
# M : 딜러가 부른 숫자
N, M = map(int, input().split())
# arr : 카드의 숫자들
arr = list(map(int, input().split()))

answer_1 = 0
for i in range (0, len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            a = arr[i] + arr[j] + arr[k]
            if M >= a > answer_1 :
                answer_1 = a
print(answer_1)