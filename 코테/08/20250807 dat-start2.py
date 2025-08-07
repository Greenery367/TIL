txt = list(map(str, input().split()))
text = 'ABCDE'

text_arr = list(text)
result = []


# text의 dat 배열 만들기
def make_dat_arr(text):
    dat_arr = [0] * 126
    for i in text_arr:
        dat_arr.append(i)
    for j in range(len(text_arr)):
        dat_arr[ord(text_arr[j])] += 1
    return dat_arr


def return_arr(txt, dat_arr):
    for i in range(len(txt)):
        if dat_arr[ord(txt[i])] == 1:
            result.append("O")
        else :
            result.append("X")
    print(*result)


# 결과 반환 메서드
result1 = make_dat_arr(text)
return_arr(txt, result1)
