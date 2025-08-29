lst = [4,5,1,1,5,4,-3,-13,9,20,13]

num = len(lst)-4
max_v = 0
idx = -2

for i in range(num):
    if sum(lst[i:i+5]) > max_v :
        max_v = sum(lst[i:i+5])
        idx = i

print(idx)