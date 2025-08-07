arr = [
    [1,2,1,3,1],
    [2,2,2,2,2,],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

i = 0
j = 1
sum_v = 0

sum_v += arr[i][j+1]
sum_v += arr[i][j-1]
sum_v += arr[i+1][j]

print(sum_v)