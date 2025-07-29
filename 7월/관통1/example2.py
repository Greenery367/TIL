var = input()

for i in range(len(var) // 2):

    if var[i] != var[len(var) - i - 1]:
        print(0)
        break
    else:
        print(1)
        break
