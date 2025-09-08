ground = [[4,5,7,6],
          [1,5,5,4],
          [1,1,1,1]]
citizen = [[5,6,4],
           [1,5,3]]

arr = [0]*8

for i in ground:
    for j in range(4):
        thing = i[j]
        arr[thing] += 1

for a in range(2):
    for b in range(3):
        person = citizen[a][b]
        print(arr[person])