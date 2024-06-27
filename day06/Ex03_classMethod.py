# 클래스메서드
# 객체를 생성하지 않아도 static 처럼 바로 사용가능
# static 과 다른 점은 cls 라는 인자가 더 추가된다.
# cls는 클래스를 가리킨다.
# @classmethod라는 데코레이터를 사용
# 주로 클래스변수를 조작하거나 생서자 대신 클래스를 초기화 하는데 사용

class Calc:
    count = 0
    @staticmethod
    def plus(a,b):
        return a+b
    def minus(self, a,b):
        return a-b
    @classmethod
    def mul(cls, a, b):
        return a*b
    @classmethod
    def countup(cls):
        cls.count += 1

if __name__ == "__main__":
    # static은 객체 생성 없이 호출 가능
    print("{0} + {1} = {2}" .format(3,5, Calc.plus(3,5)))
    # instance 객체 후  호출 가능
    c = Calc()
    print("{0} - {1} = {2}" .format(3,5, c.minus(3,5)))
    # classmethod
    print("{0} * {1} = {2}" .format(3,5, Calc.mul(3,5)))
    
    Calc.countup()
    print(Calc.count) # 1