a = 10.25
b = 20.31
sum_v = a + b
print(sum_v)

# 1. 포맷팅
print("%.1f" %sum_v)

# 2. .format() 메서드
print("{:.1f}".format(sum_v))

# 3. f-String (가장 파이써닉한 방법)
print(f'{sum_v:.1f}')

# 시퀀스 타입
# 리스트 : 가변 시퀀스
arr = [1, 2, 3, 4]
arr[0] = 10
# 문자열 : 불변 시퀀스
char = "Hello"
# char[0] = "a"