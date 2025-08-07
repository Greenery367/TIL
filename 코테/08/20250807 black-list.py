

apart_wh = list(map(int, input().split()))
apartment = [list(map(int, input().split())) for _ in range(apart_wh[0])]

black_wh = list(map(int, input().split()))
blacklist = [list(map(int, input().split())) for _ in range(black_wh[0])]


def make_black_list_dat(blacklist):
    black_dat = [0 for i in range(1000001)]
    for i in range(len(blacklist)):
        for j in range(len(blacklist[0])):
            n = blacklist[i][j]
            black_dat[n] += 1
    return black_dat

def find_criminal(apartment, black_dat):
    citizen = 0
    criminal = 0
    for i in range(len(apartment)):
        for j in range(len(apartment[0])):
            person = apartment[i][j]
            if black_dat[person] >= 1:
                criminal += 1
            else:
                citizen += 1
    print(criminal)
    print(citizen)


black_dat = make_black_list_dat(blacklist)
find_criminal(apartment, black_dat)