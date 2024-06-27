# if 조건식1 :
#    조건식1이 참일때 실행
# elif 조건식2 :    
#    조건식1이 참일때 실행
# elif 조건식 :    
#    조건식3이 참일때 실행
# [else:
#    모두 거짓일때 즉 나머지 ]

# 이름, 국어, 영어, 수학 점수를 받아서 총점, 평균, 학점을 구하자
name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))
sum = kor + eng + math
avg = int(sum/3 *100) /100
hak = ""
if(avg>=90):
    hak = "A"
elif(avg>=80):
    hak = "B"
elif(avg>=70):
    hak = "C"
else:
    hak = "F"

print("이름 : " , name)
print("총점 : " , sum)
print("평균 : " , avg)
print("학점 : " , hak)