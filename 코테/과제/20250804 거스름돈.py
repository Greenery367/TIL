money = 1000 - int(input())

result = 0
money_arr = [500, 100, 50, 10, 5, 1]

for i in money_arr :
    result += money // i
    money -= i * (money // i)
print(result)