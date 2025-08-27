from collections import deque
import sys

T = int(input())

for tc in range(1, T+1):
    p = list(input())
    n = int(input())
    string = input()
    if string == '[]' :
        print('error')
        continue
    arr = list(map(int, string.strip('[]').split(",")))
    result = 0

    for i in p:
        if i == 'R':
            temp=[]
            for i in range(len(arr)) : temp.append(arr.pop(-1))
            arr = temp

        if i == 'D' and len(arr) > 0 :
            arr.pop(0)
        elif i == 'D' and len(arr) <= 0 :
            result = 'error'

    if result == 0:
        print(arr)
    else : print(result)