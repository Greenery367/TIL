arr = ['O','X']
path = []
name = ['Luffy', 'Zoro', 'Sanji']

def print_name():
    for i in range(3):
        if path[i] == 0: # level : 3
            print(name[i], end=' ')
        print()

def KFC(lev):
    if lev == 3 : # level : 3
        print_name() # 함수호출(이름출력)
        return

    for i in range(2): # branch : 2
        path.append(arr[i])
        