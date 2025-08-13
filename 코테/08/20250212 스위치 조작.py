T = int(input())

for tc in range(T):
    bulb = list(input().split())
    goal = list(input().split())

    stack = []
    total = 0

    for i in range(len(bulb)):
        if bulb[i] != goal[i]:
            stack.append(goal[i])

    print(stack)
    print(len(stack))