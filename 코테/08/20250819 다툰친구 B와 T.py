alp = list(input())

count1 = 0
for i in range(4):
    a = alp[i]
    for j in range(4):
        b = alp[j]
        for k in range(4):
            c = alp[k]
            for f in range(4):
                d = alp[f]
                string = a+b+c+d
                if string.find('TB') != -1 or string.find('BT') != -1:
                    continue
                else : count1 += 1

print(count1)