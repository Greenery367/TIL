A = [[5,5,2,6],[9,1,1,3]]
tar = [5,6,1,1,1,1,5,4]
new=[[0]*4 for _ in range(2)]

for i in range(2):
    for j in range(4):
        for k in tar:
            if k == A[i][j]:
                new[i][j] += 1

for __ in new : print(*__)