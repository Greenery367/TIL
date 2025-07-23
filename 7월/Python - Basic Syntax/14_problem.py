temp = [0, 20, 30, 37, 100]

fahrenheit = list(map(lambda c: c * 9/5 + 32, temp))

print(*fahrenheit)
