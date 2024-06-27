# 메서드 오버라이딩 : 부모클래스의 메서드와 같은 이름으로 자식 메서드를 만들지만 내용이 다른 것 

class Animal():
    name = "휴먼"
    def sound(self):
        print("Hi~~~~")
    def eat(self):
        print("먹는다.")

class Cat(Animal):
    name = "삼색이"
    def sound(self):
        #print("야옹~~")
        pass    
        
    def prn(self):
        print(self.name)
        
class Dog(Animal):
    def sound(self):
        print("멍멍~~")    
        
    def prn(self):
        print(self.name)
        print(super().name)

if __name__ == "__main__":
    cat = Cat()
    cat.sound()
    cat.prn()
    print("-"*50)
    
    dog = Dog()
    dog.sound()
    dog.prn()
