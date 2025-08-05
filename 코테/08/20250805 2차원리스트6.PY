# 4x4 리스트
arr = []
# 4행 4열 2차원 리스트 생성
for i in range(4):
    a = list(map(int, input().split()))
    arr.append(a)

# 거꾸로 리스트 출력하기
for i in range(len(arr)-1, -1, -1):
    for j in range(len(arr)-1, -1, -1):
        print(arr[i][j], end=" ") 
    print("")   
    
    