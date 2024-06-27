# 문자열 포맷 :  %s : string,  %d : int ,   %f :float

# 숫자
print("제 나이는 %d 입니다." %20)
print("제 나이는 %d 입니다." %20.45)
print("제 나이는 %d 입니다." %20.56)

print("제 나이는 %f 입니다." %20)
print("제 나이는 %f 입니다." %20.45)
print("제 나이는 %f 입니다." %20.56)
print('-' * 30)

# 자리 지정
print("제 나이는 %5d 입니다." %20)          # 다섯자리를 차지하고 오른쪽 정렬
print("제 나이는 %3d 입니다." %24578536)    # 정부부분은 숫자가 자리보다 크면 그대로 표현

print("제 나이는 %5f 입니다." %20)          # 
print("제 나이는 %5f 입니다." %20.45)       # 
print("제 나이는 %3f 입니다." %24578536)    # 

print("제 나이는 %.2f 입니다." %20)          # 모자른건 0으로 채운다.
print("제 나이는 %.2f 입니다." %20.444)      # 반올림 됨
print("제 나이는 %.2f 입니다." %20.445)      # 반올림 됨

# 전체길이 10개 소수점 4자리 차지 
print("제 나이는 %10.4f 입니다." %3.145 )

age = 34 
name = "고길동"

print("저의 이름은 %s 입니다.\n저의 나이는 %d 입니다.\n저의 키는 %.1f 입니다." % (name, age, 181.2504))
print("저의 이름은 %s 입니다.\n저의 나이는 %d 입니다.\n저의 키는 %.1f 입니다." % ({name, age, 181.2504}))
print('-' * 30)

print("저의 이름ㅇㄴ {} 입니다." .format(name))
print("저의 ㄴ아ㅣㄴ {} 입니다." .format(age))
print("저의 키는 {} 입니다." .format(181.2504))
print('-' * 30)



print("저의 이름은 {0} 입니다. \n저의 나이는 {1} 입니다. \n저의 키는 {2:.1f} 입니다.".format(name, age, 181.2504))