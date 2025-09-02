T = int(input())

for tc in range(T):
    a,b = map(int, input().split())
    max_v = a*b
    while b:
        a,b = b, a%b
    print(max_v // a)