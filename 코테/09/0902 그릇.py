dish = input()
result = 0
for i in range(len(dish)):
    if i == 0 : result += 10
    elif dish[i] == dish[i-1] : result += 5
    else: result += 10
print(result)