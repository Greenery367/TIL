N = int(input())
result = 666
count = 1

while True:
    if count == N and '666' in str(result):
        print(result)
        break

    if '666' in str(result):
        count += 1

    result += 1