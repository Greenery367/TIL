arr = [[1,5,10,15], [15,15,20,20]]

n = int(input())

# make_dat_arr() : dat 배열 만드는 함수
def make_dat_arr(arr) :
    biggest = 0
    if max(arr[0]) > max(arr[1]) : biggest = max(arr[0])
    else : biggest = max(arr[1])

    dat_arr = []
    for i in range(0, biggest+1):
        dat_arr.append(0)
    return dat_arr

# check_nums() : dat_arr를 사용한 함수
def check_nums(arr, dat_arr):
    for i in range(2):
        for j in range(4):
            dat_arr[arr[i][j]] += 1
    return dat_arr

# dat 배열 만들기
result1 = make_dat_arr(arr)
result2 = check_nums(arr, result1)
print(result2[n])