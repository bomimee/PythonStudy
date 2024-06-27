
str = "hobby"
print(str.count("b"))

print(str.find("b"))
print(str.find("k")) # 없으면 -1 반환

print(str.index("b"))
#print(str.index("k")) # 없으면 오류

print(",".join(str))

print(str.upper()) #

print((str.upper()).lower())

str = "  hello "
#remove left space - lstrip 
#remove right space - rstrip

print(str.lstrip(), len(str.lstrip()), len(str)) 
print(str.rstrip(), len(str.rstrip()), len(str)) 

str = 'Life is too short'
print(str.replace("Life", "Your leg"))

print(str.split())