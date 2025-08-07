text = 'BBQBHCBTS'

def make_dat_array(text):
    # 문자열의 아스키코드 번호를 담은 리스트
    text_arr = list(map(ord, list(text)))
    max_v = max(text_arr)
    dat_arr = []

    # dat_arr 만들기
    for i in range(0, max_v+1):
        dat_arr.append(0)

    for j in text_arr:
        dat_arr[j] += 1
    print(max(dat_arr))
    return dat_arr
make_dat_array(text)