# 1. 문자열 입력 받기
char = input()

# 2. 정수 입력 받기
num = int(input())

# 3. 정수 여러개 입력 받아서 각각의 변수에 할당
# map 함수, split() 메서드
a, b = map(int, input().split())

# 4. 정수 여러 개를 입력 받아서 리스트에 할당
arr = list(map(int, input().split()))

# 5. 심화 2차원 리스트를 입력받기 (D3 난이도)
# 반드시 어떤 로직을 써야 할까? : 중첩 반복문
# --> 리스트 컴프리헨션

result = []
for _ in range(3): # 3행
    arr = list(map(int, input().split()))
    result.append(arr) # 행 추가 * 3번
print(result)    

arr = [list(map(int, input().split())) for _ in range(3)]