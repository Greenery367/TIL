# flag 처리 : flag 변수를 bool 타입 변수로 활용
A = [4,2,5,3,7,6]
B = [5,3,7]

n = int(input())
flag = True
for i in range(0, len(B)):
    if A[n+i] != B[i]:
        flag = False
        break
if not flag : print("X")
else : print("O")