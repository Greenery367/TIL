T = int(input())
total = []
for tc in range(T):
    total_v = 0
    s = list(map(int, input().split()))
    if s[0] == s[1] == s[2] : total_v += 10000 + s[0]*1000
    elif s[0] == s[1]: total_v += 1000+ s[0] * 100
    elif s[1] == s[2]: total_v += 1000 + s[1] * 100
    elif s[0] == s[2]:total_v += 1000 + s[2] * 100
    else: total_v += max(s) * 100
    total.append(total_v)
print(max(total))