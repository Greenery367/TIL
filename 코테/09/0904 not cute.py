N = int(input())
a = 0
b = 0

for n in range(N):
    var = int(input())
    if var == 0 : a+=1
    else: b+=1

if a>b : print("Junhee is not cute!")
else: print("Junhee is cute!")