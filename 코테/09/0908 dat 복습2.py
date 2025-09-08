txt = 'BBQBHCBTS'

arr=[0]*200

for i in txt:
    arr[ord(i)] += 1

print(max(arr))