# 단순 if : 조건이 참일 때만 실행, 거짓이면 if문 무시

# if 조건식:
#   조건식이 참일때 실행
#   조건식이 참일때 실행

# 주의 사항 : 반드시 들여쓰기를 해야 하고 일정해야 한다.
# switch, case 라는 키워드는 존재하지 않음
# 조건식은 boolean형 ,  and, or, not

# 입력받은 값이 60이상이면 합격
su1 = int(input("데이터 입력 >> "))
if(su1>=60):
    print("합격")

# 입력받은 값이 홀수인지, 짝수인지 
res = "짝수"
if(su1%2==1):
    res="홀수"
    
print(res)