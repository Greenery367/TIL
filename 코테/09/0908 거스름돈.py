a = int(input())
arr = [500,100,50,10]
result = 0

for i in arr:
    if i <= a :
        result += a // i
        a = a % i
    else:
        continue

print(result)
