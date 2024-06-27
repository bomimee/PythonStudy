class Animal():
  name="human"
  def sound(self):
    print("hi~~~")
  def eat(self):
    print("eat")
    
    
class Cat():
  name="samsac"
  def sound(self):
    print("meow~~~")
  def prn(self):
    print(self.name)
    
    
class Dog(Animal):
  def sound(self):
    print("bow wow~~~")
  def prn(self):
    print(self.name)
    print(super().name)
    
if __name__ == '__main__':
  cat = Cat()
  cat.sound()
  