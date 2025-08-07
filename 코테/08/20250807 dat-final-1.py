ground = [
    [4,5,7,6],
    [1,5,5,4],
    [1,1,1,1]
]

citizen = [
    [5,6,4],
    [1,5,3]
]

max_c = 0
if max(citizen[0]) > max(citizen[1]) :
    max_c = max(citizen[0])
else : max(citizen[1])

def make_dat_arr(citizen):
    dat_arr = [0] * (max_c)
    return dat_arr

def compare_c_g(dat_array, ground, max_c):
    for i in range(3):
        for j in range(4):
            if ground[i][j] <= max_c :
                dat_array[ground[i][j]-1] += 1

    for k in range(2):
        for j in range(3):
            print(dat_array[citizen[k][j]-1], end = " ")
        print("")

dat_array = make_dat_arr(citizen)
compare_c_g(dat_array, ground, max_c)