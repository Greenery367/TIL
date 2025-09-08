TXT = 'ABCDE'

arr = list(input().split())

for i in range(len(arr)):
    if arr[i] in TXT :
        print('O', end=' ')
    else:
        print('X', end=' ')