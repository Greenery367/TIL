
# 5x5 크기의 2차원 배열 생성
div5_arr=[]

num_of_two = 0
biggest = -1
smallest = 1000
total = 0

# for문 순회로 원소 삽입
for i in range(5):
    var = list(map(int, input().split()))
    div5_arr.append(var)

for j in range(len(div5_arr)):
    for k in range(len(div5_arr)):
        # 1. 2의 개수 구하기
        if div5_arr[j][k] == 2 :
            num_of_two += 1
        # 2. 최대값 찾기
        if div5_arr[j][k] > biggest:
            biggest = div5_arr[j][k]
        # 3. 최소값 찾기
        if div5_arr[j][k] < smallest:
            smallest = div5_arr[j][k]
        # 4. 대각선 요소들 합계 구하기
        if j == k :
            total += div5_arr[j][k]
            
print(num_of_two)
print(biggest, smallest)
print(total)