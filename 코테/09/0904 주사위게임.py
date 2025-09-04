c, s = 100, 100
T = int(input())

for tc in range(T):
    a, b = map(int,input().split())
    if a>b : s -=a
    elif a<b : c-=b
    else: continue

print(c)
print(s)