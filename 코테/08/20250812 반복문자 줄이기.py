T = int(input())

for i in range(1, T+1):
    a = input()
    stack = [a[0]]

    for j in range(1, len(a)):
        if stack and a[j] == stack[len(stack)-1]:
            stack.pop()

        else:
            stack.append(a[j])

    print(f"#{i} {len(stack)}")