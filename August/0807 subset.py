def print_subset(bit):
    for i in range(4):
        if bit[i]: # if i가 0이 아니면
            print(arr[i], end = ' ')
    print(bit)

arr = [7, 5, 8, 1]
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(3):
                bit[3] = l
                print_subset(bit)