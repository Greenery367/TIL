S = int(input())
idx = 1
current = 0
result = 0
while True:
    if current + idx <= S :
        current += idx
        idx += 1
    else:
        print(idx - 1)
        break