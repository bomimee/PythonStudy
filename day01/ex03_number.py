# 숫자형 : 정수,  실수, 복소수, 8진수, 16진수

# 1.정수 : 소수점이 없는 숫자
age = 28
print(age,  type(age))

# 2.실수 : 소수점이 있는 숫자
weight = 92.4
print(weight,  type(weight))

# 3.실수형지수 ( 컴퓨터식 지수 표현)
height = 1.812E2  # 1.812e2   => 1.812 * 10^2 
print(height, type(height))

# 4.복소수 : 실수부와 허수부 
num = 412 + 34j
print(num, type(num))

# 실수부만 추출
print(num.real , type(num.real))

# 허수부만 추출
print(num.imag, type(num.imag))

# 8진수 : 0o 시작
num = 0o10
print(num, type(num))

# 16진수 : 0x 시작
num = 0x10
print(num, type(num))

print('-' * 30)

# 정수를 실수로 변환
num = 27 
res = float(num)
print(res, type(res))

# 실수를 정수로 변환
num = 28.524
res = int(num)
print(res, type(res))

# 소숫점 둘째자리 까지 구하기 
num1 = 27.444
num2 = 27.445
numm = 28.524 
res = int(numm *10) /10
print("-")
print(res)
print("-")
# 반올림 안됨
res1 = int(num1 * 100) /100
res2 = int(num2 * 100) /100
print(res1)
print(res2)
str = "python " * 5
print(str)
# 반올림 됨
print('%.2f' %num1)
print('%.2f' %num2)

# 일의 자리 버림
res1 = int(num1 / 10) * 10
res2 = int(num2 / 10) * 10
print(res1)
print(res2)

