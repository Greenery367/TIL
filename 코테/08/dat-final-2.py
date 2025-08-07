criminal = [
    [5,7,9,55],
    [30,10,6,8]
]

apartments = [
    [1,2,3,4],
    [5,7,10,15]
]



def make_criminal_list(criminal):
    max_v = max(max(criminal[0]),max(criminal[1]))
    criminal_dat = [0] * (max_v+1)

    for i in range(2):
        for j in range(4):
            criminal_dat[criminal[i][j]] += 1
    return criminal_dat

def find_criminal(criminal_dat, apartments):
    citizen = 8
    evils = 0
    for i in range(len(criminal_dat)):
        if criminal_dat[i] == 1 and (apartments[0].count(i) != 0 or apartments[1].count(i) != 0):
            evils += 1
            citizen -= 1
    print(evils, citizen)

criminal_dat = make_criminal_list(criminal)
find_criminal(criminal_dat, apartments)