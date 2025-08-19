path = []

def KFC(level):

    if level == 2: # level = 2
        print(path)
        return

    for i in range(3):
        path.append(i)
        KFC(level+1)
        path.pop()

# 순열(중복순열에 used 배열 사용)
# 주사위 3개를 던져 나올 수 있는 순열
def KFC2(level):
    if level == 3:
        print(path)
        return

    for i in range(1, 7): # branch = 6
        if used[i] == 1 : continue
        path.append(i)
        KFC2(level+1)
        path.pop()
        used[i] = 0

KFC(0)

# 부분 집합은 항상 branch가 2인 중복 순열 (o, x)
# 다섯명으로 이루어진 부분집합 : level -> 5
arr = ['O', 'X']
path = []
name = ['A', 'B', 'C', 'D', 'E']

def KFC3(level):
    if level == 5 :
        print(name)
        return

    for i in range(2): # branch = 2
        path.append(arr[i])
        KFC(level+1)
        path.pop()

# 조합
# abc와 bac는 같은 조합
# 순열이라면 둘은 다른 조합임! (순서가 중요함)
# 조합에서의 핵심 = 앞에서 뽑은 경우의 수를 제외하고 시작하는 것(start 매개변수 추가)

arr = ['A','B','C','D','E']
path = []

def