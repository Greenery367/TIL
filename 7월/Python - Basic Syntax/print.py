

## print 함수에 대해 알아보자.
## sep default 값 : 공백
## end default 값 : /n
print("오늘 점심은 묵은지 해장국 예~")

## end 값을 다르게 할당해주면 줄바꿈이 사라진다.
print("hello world" , end = " ")
print("배고팡")
# 결과 => hello world 배고팡

## 할당 Reassignment
## 할당과 저장의 차이?

degree = 36.5 ## degree에 36.5라는 값이 할당
print(id(degree)) ## degree의 주소값 출력
degree = 36.6
print(id(degree)) ## 다른 값이 할당된 degree의 주소값 출력

## 왜 첫번째와 두번째의 id가 다를까?
## degree는 이름표의 개념이기 때문
## degree는 뗐다 붙일 수 있는 변수명

## 변수명은 숫자로 시작되면 안된다
song99 = 11
# 99song = 11

## 언더스코어 가능
song_eom = 11
eom_song = 11
_song = 11

## 키워드(예약어) 사용 불가능 
## 내장함수, 메서드 등은 가급적 사용하지 않는다.
# if false true while for sum ...
lst = [1, 2, 3]
print(sum(lst)) # 결과 6

list1 = [1, 2, 3, 4]
arr = list((1, 2, 3, 4))
print(sum(arr)) # 결과 10

print(ord('A')) ## ASCII 코드 값 A
print(ord('B')) ## ASCII 코드 값 B

print(id(lst))
print(lst)
lst = [1, 1, 1, 1]
print(id(lst))