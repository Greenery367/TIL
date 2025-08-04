arr = []
for i in range(9):
    inner_arr = list(map(int, input().split()))
    arr.append(inner_arr)
    
biggest_one = -1
width = 0
height = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > biggest_one :
            biggest_one = arr[i][j]
            width = i+1
            height = j+1
            
print(biggest_one)
print(width, height)