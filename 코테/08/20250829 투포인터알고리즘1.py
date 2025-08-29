

n,m = map(int, input().split())
arr = list(map(int, input().split()))
a = 0
b = 0

for i in range(n-1):
    if arr[i]+arr[i+1] == m : a,b = i,i+1

if a+b == 0 : print('찾을 수 없음')
else: print(a,b)