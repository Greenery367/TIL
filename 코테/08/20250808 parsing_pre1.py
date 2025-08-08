a = input()

def is_palindrome(txt):
    stop = len(txt) // 2
    flag = True

    for i in range(1, len(txt)):
        if txt[i-1] != txt[len(txt)-i]:
            flag = False

    if flag == False:
        print(0)
    else :
        print(1)

is_palindrome(a)