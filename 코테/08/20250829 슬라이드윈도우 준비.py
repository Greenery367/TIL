lst = [4,5,1,1,5,4,-3,-13,9,20,13]
idx = int(input())

def get_sum(arr, idx):
    return sum(arr[idx:idx+5])

print(get_sum(lst,idx))