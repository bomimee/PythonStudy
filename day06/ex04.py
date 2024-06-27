# 상속 : 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을 수 있게 만드는것 

# 형식) class 클래스_이름(상속할 클래스이름)
class Animal():
  def eat(self):
    print("eat")
  
  def play(self):
    print("exercise")
    
class Human(Animal):
  def wave(self):
    print("손을 흔들다")
    
class Dog(Animal):
  def wave(self):
    print("꼬리를 흔들다")

if __name__=="__main__":
  human = Human()
  human.eat()
  human.play()
  human.wave()
  
  dog = Dog()
  dog.eat()
  dog.play()
  dog.wave()   