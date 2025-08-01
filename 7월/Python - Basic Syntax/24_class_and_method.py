class Calculator:
    pi = 3.141592 # 클래스 변수

    # 생성자
    def __init__(self, name):
        self.name = name # 인스턴스 변수

    # 메서드
    def add(self, a, b):
        return a + b
    
    # 매직 메서드 --> 객체를 문자열로 표현할때 호출됨
    def __str__(self):
        return f'Calculator name : {self.name}'
    
    # 클래스 메서드 --> 클래스 자체를 첫번째 인자로 받는다
    @classmethod
    def get_pi(cls):
        return f'파이 값은 {cls.pi}'
    
    # 스태틱 메서드 --> self나 cls가 없음, 독립적으로 실행 가능
    @staticmethod
    def multiply(a, b):
        return a * b

# 인스턴스 생성
calc = Calculator("공학용계산기")
# 메서드 호출
print(calc.add(2, 3))
# 매직 메서드 호출 - 인스턴스를 할당한 변수만 작성
print(calc)
# 클래스 메서드 호출 - 클래스로 직접 호출
print(Calculator.get_pi())
# 스태틱 메서드 호출 - 클래스로 호출도 가능, 인스턴스로 호출도 가능
print(Calculator.multiply(4, 5))
print(calc.multiply(4, 5))