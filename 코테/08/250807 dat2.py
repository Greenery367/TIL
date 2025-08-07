A = [5,7,5,4,2,9]
B = [5,4,2,5,6]

arr = []

for i in A:
    if B.count(i) != 0 :
        arr.append('O')
    else :
        arr.append('X')

print(*arr)