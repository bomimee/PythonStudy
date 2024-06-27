class Calc:
  
  count = 0
  
  @staticmethod
  def plus(a,b):
    return a+b
  
  def minus(self, a,b):
    return a-b
  @classmethod
  def mul(cls, a,b):
    return a*b
  @classmethod
  def countup(cls):
    cls.count += 1
    
if __name__=="__main__":
  #static은 객체 생성 없이 호출가능
  print("{0} + {1} = {2}" .format(3,5, Calc.plus(3,5)))
  
  c=Calc()
  print("{0} - {1} = {2}" .format(3,5, c.minus(3,5)))
  
  #classmathod
  print("{0} * {1} = {2}" .format(3,5, c.mul(3,5)))