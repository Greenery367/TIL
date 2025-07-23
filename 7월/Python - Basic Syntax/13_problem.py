cnt = 0 

def factorial(n) :
    
    global cnt
         
    if n == 1 :
        cnt += 1
        return 1
    else :
        cnt += 1
        return n * factorial(n-1)
    
factorial(5)
print(cnt)