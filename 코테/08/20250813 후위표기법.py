T = int(input())

for tc in range(1, T+1):
    question = list(input().split())
    stack = []
    flag = True
    arr = ['+','-','*', '/']
    for i in range(len(question)):
        if question[i] == '.' : break

        elif len(stack) == 1  and question[i].isdecimal() == False :
            flag = False

        if question[i].isdecimal(): stack.append(question[i])

        elif len(stack) > 1 :
            if question[i] == arr[0]:
                a = int(stack.pop()) + int(stack.pop())
                stack.append(a)
            elif question[i] == arr[1]:
                aa = int(stack.pop())
                bb = int(stack.pop())
                a = bb-aa
                stack.append(a)
            elif question[i] == arr[2]:
                a = int(stack.pop()) * int(stack.pop())
                stack.append(a)
            elif question[i] == arr[3]:
                aa = int(stack.pop())
                bb = int(stack.pop())
                a = int(bb/aa)
                stack.append(a)
        else : break

    if flag == True and len(stack) == 1 : print(f"#{tc} {stack[0]}")
    else : print(f"#{tc} error")