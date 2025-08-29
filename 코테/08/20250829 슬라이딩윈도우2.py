lst = [4,5,1,1,5,4,-3,-13,9,20,13]

def get_sum(arr):
    num = len(arr) - 4
    max_v = -100
    result = -2
    for i in range(num):
        var = sum(arr[i:i+5])
        if max_v < var :
            max_v = var
            result = i
    return result

print(get_sum(lst))