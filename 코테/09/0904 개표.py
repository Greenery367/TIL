N = int(input())
arr=input()

if arr.count('A') > arr.count('B') : print('A')
elif arr.count('B') > arr.count('A') : print('B')
else: print("Tie")