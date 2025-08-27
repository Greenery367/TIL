T = int(input())

for tc in range(1, T+1):
    line = input()
    stack = []
    result = ''

    for ch in line:
        if ch == '.':
            while stack:
                result += stack.pop()
            result += '.'
        else:
            stack.append(ch)

    while stack:
        result += stack.pop()

    print(f"#{tc} {result}")