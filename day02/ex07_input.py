# input 키보드로 정보를 입력 받아서 처리할 수 있다. 
# input 으로 들어온 정보는 문자열이다.

name = input("이름을 입력하세요 >> ")

kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))

sum = kor + eng + math
avg = sum/ 3
avg2 = int(avg*100)/100

if avg2 >=90:
  hak = "A"
elif avg2 >=80:
  hak  ="B"
elif avg2 >=70:
  hak = "C"
else :
  hak = "F"
  
print("이름 : " , name)
print("총점 : " , sum)
print("평균 : " , avg2)
print("학점 : " , hak)

