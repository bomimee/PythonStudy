class Human:
  name = "둘리"
  age = 5
  
  def dis_print(self):
    print("{0}살 {1} 입니다" .format(self.age, self.name))
    
#객체생성    
person = Human()    

person.dis_print()

class Human2:
  def __init__(self, name, age):
    self.age = age
    self.name = name
    
  def dis_print(self):
      print("{0}살 {1} 입니다" .format(self.age, self.name))
      
 
person2 = Human2("홍길동", 24)
person2.dis_print()



person.dis_print()

class Human3:
  name = "둘리"
  age = 5
    
  def __init__(self, name, age):
    self.age = age
    
  def dis_print(self):
    print("{0}살 {1} 입니다" .format(self.age, self.name))

person3 = Human3("고길동", 24)
person3.dis_print()

Human3("희동이", 3).dis_print()      