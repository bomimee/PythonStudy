# if ~ else 
# if 조건식:
#     조건식이 참일때 실행
# else:
#     조건식이 거짓일때 실행

# 받은 점수가 80이상이면 합격, 아니면 불합격
su1 = int(input("점수입력 : "))
res = ""
if(su1 >= 80):
    res = "합격"
else:
    res = "불합격"
    
print("결과 : " , res)

# 받은 숫자가 홀수인지, 짝수인지 판별 
su2 = int(input("숫자입력 : "))
res2 = ""
if(su2 %2 == 0):
    res2 = "짝수"
else:
    res2 = "홀수"
    
print("결과 : " , res2)