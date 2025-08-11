money = [500, 100, 50, 10]
total = 0
have = int(input())

for i in range(4):
    nums = have // money[i]
    total += nums
    have -= nums * money[i]

print(total)