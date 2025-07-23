# 0부터 4까지 출력 
for i in range(5):
    print(i, end=" ")

print()
    
# 3부터 12까지 3의 배수 출력
for i in range(1, 5):
    print(i*3, end=" ")
    
print()
    
# 20부터 -10까지 5의 배수 출력
for i in range(20, -11, -1):
    if(i % 5 == 0):
        print(i, end = " ")
        