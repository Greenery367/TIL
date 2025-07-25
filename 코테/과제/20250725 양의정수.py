sum = 0

while True :
    a = int(input())
    
    if a < 0 :
        print(sum)
        sum = 0
        
    elif a > 0 :
        sum += a
    
    else :
        print(sum)
        break
        