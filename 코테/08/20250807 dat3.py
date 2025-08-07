A = [5,2,5,7,3]
n = int(input())

def get_count(n, A):
    result = 0
    for i in A:
        if i == n :
            result += 1

    print(result)

get_count(n, A)