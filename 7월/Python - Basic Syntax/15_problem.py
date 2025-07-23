a, b, c = map(str, input().split())
money = 0

if a == b == c :
    money = 10000 + int(a) * 1000
elif (a == b) or (a == c) or (b ==c) :
    a_num = str(a+b+c).count(a)
    b_num = str(a+b+c).count(b)
    c_num = str(a+b+c).count(c)
    
    if a_num >= b_num and a_num >= c_num:
        money = 1000 + int(a) * 100
    elif b_num >= a_num and b_num >= c_num :
        money = 1000 + int(b) * 100
    else :
        money = 1000 + int(c) * 100
else :
    aa = [a, b, c]
    aa.sort(reverse = True)
    money = int(aa[0]) * 100
    
print(money)