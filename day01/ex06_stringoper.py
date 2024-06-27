# escape => \n, \t, \' \" 

#문자열 연산 + , *

#문자열 길이 구하기
str = "hello nice to meet you"
print(len(str))

# 인덱싱 : 원하는 위치 지정
#슬라이싱: 잘라내기

# 인덱싱: 0~ 왼쪽에서 오른쪽, 음수인경우는 오른쪽부터 왼쪽으로 

str = "hello pyton"
print(str[6])
print(str[-1])
print(str[-5])

# 원하는 위치에서 원하는 갯수만큼 추출
print(str[6:8], type(str[6:8]))
# print(str[-3:-5], type(str[-3:-5]))  => 잘못됨
print(str[-5:-3], type(str[-5:-3]))

#중간부터 끝까지 추출
print(str[6:])
print(str[6:12])
#전체
print(str)
print(str[:])

#틀린글자 변경하기
# 가변현 자료형 : list, dict, set, => 추가 삭제 수정 가능
# 불변형 자료형 : str, tuple => 수정 불가

# str = "pithon"

# str[1] = 'y'

#

age = 34
name = '고길동'

print("저의 이름은 %s 입니다.\n 저의 나이는 %d 입니다. \n 저의 키는 %.1f 입니다." %(name, age, 181.2504))
