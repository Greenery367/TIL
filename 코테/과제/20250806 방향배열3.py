arr = [
    [1,2,1,3,1],
    [2,2,2,2,2,],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

var = list(map(int, input().split()))

sum_v = 1

sum_v *= arr[var[0]][var[1]]
sum_v *= arr[var[0]-1][var[1]-1]
sum_v *= arr[var[0]-1][var[1]+1]
sum_v *= arr[var[0]+1][var[1]-1]
sum_v *= arr[var[0]+1][var[1]+1]

print(sum_v)