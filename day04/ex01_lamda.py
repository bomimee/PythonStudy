str = lambda : "hello"
print(str)

str2 = lambda a, b : a+b
res = str2(7,10)
print(res)

def str3(a,b) :
  return a+b
res = str3(7,10)
print(res)

def find_max(lis):
  n = len(lis)
  max_v= lis[0]
  for i in range(1,n):
    if(lis[i] > max_v):
      max_v = lis[i]
      return max_v
    
lis= [17, 92, 32,18,55,45, 90]
print(find_max(lis))

def find_same_name(lis2):
  n = len(lis2)
  result = set()
  for i in range(0, n-1):
    for j in range(i+1, n):
      if(lis2[i]==lis2[j]):
        result.add(lis2[i])  #추가 : list => append, set => add
  return result  

  
name=["tom", "jerry", "mike", "tom", "hong"]
print(find_same_name(name))