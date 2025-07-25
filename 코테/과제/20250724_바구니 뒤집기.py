a = str(input())
aa = "abcdefghijklmnopqrstuvwxyz"
arr = []
result_arr = []

# 배열 만들기
for i in range(0, len(aa)-1) :
    arr.append(aa[i])
    result_arr.append(-1)

for i in a :
    if arr.count(i) :
        
print(arr)