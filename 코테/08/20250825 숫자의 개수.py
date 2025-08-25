lst = []
for f in range(3):
    lst.append(int(input()))

arr = [0 for i in range(1,11)]

total = str(lst[0]*lst[1]*lst[2])

for j in total: arr[int(j)] += 1

for k in arr : print(k)