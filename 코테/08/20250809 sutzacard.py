T = int(input())

for i in range(T):
    a = input()
    text = list(input())
    
    biggest = 0
    most = 0
    
    for b in text:
        if text.count(b) > most :
            biggest = int(b)
            most = text.count(b)
        if text.count(b) == most and biggest < int(b):
            biggest = int(b)
            most = text.count(b)
            
    print(f"#{i+1} {biggest} {most}")
    