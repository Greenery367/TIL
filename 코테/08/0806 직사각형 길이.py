T = int(input())

for i in range(T):
    arr = list(map(int, input().split()))
    answ = 0
    for j in arr:
        if arr.count(j) != 2:
            answ = j
            pass
    print(f"#{T} {answ}")