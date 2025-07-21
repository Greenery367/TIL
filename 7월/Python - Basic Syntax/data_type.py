a = 1
b = 0.5
c = "묵은지 해장국"
d = 3 + 2j

print(type(a)) # int
print(type(b)) # float
print(type(c)) # str
print(type(d)) # complex 복소수

# Numeric Type
# 정수 : 음의 정수, 양의 정수, 0
a_num = 2
b_num = 2.0
print(a_num == b_num) # 값이 동일하다
print(type(a_num)) # int
print(type(b_num)) # float
# a_num과 b_num은 값이 동일하나 타입이 다르다!

# 1억 지수 표현법
a = 1e8 # 1억을 지수 표현법으로 표기
b = 1e3 # 1000을 지수 표현법으로 표기

# 가장 헷갈리면서 가장 중요한 부호
# /, //, %
print(10/3) # 나눗셈 : 3.33333333
print(10//3) # 나눗셈(몫) : 3
print(10%3) # 나눗셈(나머지) : 1


## 문자 시퀀스 타입
char = "hello world"
# 공백도 포함된다!
a = ' '
print(ord(a)) # 32 : 공백도 ASCII 코드 값을 가지고 있다

print('"안녕하세요"')


name = "쏭현"
age = 27
height = 163.5

print(f"내 이름은 {name}이고, 올해로 {age}야. 키는 {height:.0f}cm야.")
