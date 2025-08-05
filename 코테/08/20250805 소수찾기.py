N = int(input())
num_arr = list(map(int, input().split()))
total = 0

for i in num_arr:
    if i == 0 or i == 1:
        continue  # 0과 1은 소수가 아님

    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break  # 나눠지는 수가 있으면 소수 아님

    if is_prime:
        total += 1

print(total)
