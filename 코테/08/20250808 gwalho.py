text = input()
n = len(text)
a,b = 0, 0
sum_v = 0
i = 0 # while 문 초기식
while i<n: # while 문 조건식
    # 덧셈 계산
    if text[i] == '[':
        a = i
        b = text.find(']', a+1)
        sum_v += int(text[a+1:b])
        i += (b - a) # +1은 증감식에서
    # 곱셈 계산
    elif text[i] == '{':
        a = i
        b = text.find('}',a+1) # 열리는 위치 이후로
        sum_v *= int(text[a+1:b])
        i += (b - a) # +1은 증감식에서

    i += 1 # 증감식

print(sum_v)
