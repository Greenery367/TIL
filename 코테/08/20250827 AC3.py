from collections import deque

T = int(input())

for tc in range(1, T+1):
    function = input()
    n = int(input())
    n_arr = input()[1:-1]
    arr = n_arr.split(',')

    queue = deque(arr)
    reversed = 0
    flag = False

    if n == 0 or n_arr == '':
        queue = deque()
        flag = True

    for i in function:
        if i == 'R':
            reversed += 1

        else:
            if reversed % 2 == 1:
                queue.pop()
            else:
                queue.popleft()

    if flag == True:
        print('error')
    else:
        if reversed % 2 == 1 :
            queue.reverse()
        print("[" + ','.join(queue) + ']')