T = int(input())

for tc in range(T):
    r,e,c = map(int, input().split())
    if e > c and e-c>r: print("advertise")
    elif e < c : print("do not advertise")
    else: print("does not matter")