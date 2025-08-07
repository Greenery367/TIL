arr = [
    [1,2,1,3,1],
    [2,2,2,2,2,],
    [1,0,1,0,1],
    [3,1,2,1,3]
]

var = list(map(int, input().split()))

# arr = [arr[var[0]-1][var[1]], arr[var[0]+1][var[1]]
#        , arr[var[0]][var[1]+1], arr[var[0]+1][var[1]+1]]

print(max(arr))