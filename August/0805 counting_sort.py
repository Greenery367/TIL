def counting_sort(arr, k, result):
    dat = [0] * (k+1)

    # 카운팅 정렬 1단계 : 값 -> 인덱스
    for i in range(len(arr)):
        dat[arr[i]] += 1

    # 카운팅 정렬 2단계 : 누적
    for i in range(1, k+1):
        dat[i] += dat[i-1]

    # 카운팅 정렬 3단계 : 뒤에서부터 정렬된 배열 생성
    for i in range(len(arr)-1, -1, -1):
        dat[arr[i]] -= 1
        result[dat[arr[i]]] = arr[i]

arr = [12, 3, 9, 1, 15, 7]
k = 15
result = [0] * len(arr)
counting_sort(arr, k, result)

print(result)