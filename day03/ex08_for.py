# for 변수 in 리스트, 튜플, 집합, 딕셔너리, 문자열:
#     수행할 문장      
#     수행할 문장
#     수행할 문장

# 리스트
t_list = ["one", "two", "three"]
for i in t_list:
    print(i)
print("-" * 50)

# 튜플
t_tuple = ("red", "green", "blue")
for i in t_tuple:
    print(i)
print("-" * 50)    

# 집합 (순서가 없이 나온다)
t_set = {"하나", "둘", "셋"}
for i in t_set:
    print(i)
print("-" * 50)    

# 딕셔너리
t_dic = {"name" : "hong", "phone":"010-9797-7979", "addr":"seoul" , "age" : 24}
for i in t_dic.keys():
    print(i)
print("-" * 50)    

t_list = [(1,2), (3,4), (5,6)]
for (i, j) in t_list:
    print(i + j)
    
t_dic = {"name" : "hong", "phone":"010-9797-7979", "addr":"seoul" , "age" : 24}
for k, v in t_dic.items():
    print(k , ":", v)


str2 = lambda a, b : a*b
res = str2(7,10)
print(res)
