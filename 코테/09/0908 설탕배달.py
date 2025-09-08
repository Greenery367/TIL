N = int(input())

cnt_f = 0 # 5
cnt_t = 0 # 3

idx_f = 0
idx_t = 0

while True:
    if idx_f*5 == N:
        break
    elif (idx_f+1)*5 >= N:
        if N - idx_f*5 == 3 :
            idx_f += 1
            break
    idx_f += 1

while True:
    if idx_t*3 == N or (idx_t+1)*3 >= N:
        break
    idx_t += 1

print(idx_f, idx_t)