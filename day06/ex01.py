#인스턴스 변수 : 일반변수, 객체가 생성되면서 같이 생성되는 변수.. self가 붙어있다

class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
    
  def prn(self):
      print("name: ", self.name)
      print("age: ", self.age)
      
if __name__=="__main__":
  man = Person("홍길동", 37)
  man.prn()
  
  woman = Person("원더우먼", 24)
  woman.prn()
  