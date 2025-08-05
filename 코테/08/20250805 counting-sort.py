var = [12, 3, 9, 1, 15, 7]

def counting_sort(arr):
    temp_arr = [0] * len(var)
    max_var = max(var)
    count_arr = [0] * (max_var + 1)
    
    # 카운팅 배열 만들기
    for i in range(len(arr)) :
        count_arr[arr[i]] += 1
    
    # 카운트 값 조정
    for j in range(1, max_var+1) :
        count_arr[j] += count_arr[j-1]
    
    # 3단계 :
    for k in range(len(arr)-1, -1, -1):
        count_arr[arr[k]] -= 1
        temp_arr[count_arr[arr[k]]] = arr[k]
        
    return temp_arr

print(*counting_sort(var))