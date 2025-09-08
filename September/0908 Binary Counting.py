arr = [1,2,3,4]

# i  0~2^n == i번째 부분집합
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end="")
    print()