arr = [4,5,1,1,5,4,-3,-13,9,20,13]

sum_v = sum(arr[:5])
max_v = sum_v
max_idx = 0

for i in range(len(arr)-5):
    sum_v -= arr[i]
    sum_v += arr[i+5]

    if sum_v > max_v:
        max_v = sum_v
        max_idx = i + 1
