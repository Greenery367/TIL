T = int(input())

for i in range(T):
    var = input()
    result = 0
    arr=[]
    flag = True
    for j in range(len(var)):
        if arr.count(var[j]) > 0 and var[j] != var[j-1]:
            flag = False
            continue
            
        arr.append(var[j])
        if j == len(var)-1 and flag == True:
            result += 1
    
                
    
    
print(result)