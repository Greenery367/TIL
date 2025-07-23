hour, min = map(int,input().split())
req_time = int(input())

total_time = hour*60 + min + req_time

hour = total_time // 60
min = total_time % 60

if hour >= 24 :
    hour -= 24
    
print(f"{hour} {min}")