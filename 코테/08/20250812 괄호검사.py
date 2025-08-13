T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []
    is_valid = True

    for ch in text:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = False
                break
        elif ch == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False

    print(f"#{tc} {1 if is_valid else 0}")
