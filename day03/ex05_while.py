# 초기식
# while 조건식:
#    수행할 문장1
#    수행할 문장2
#    수행할 문장3
#    증감식

# 1 부터 10 까지 출력
su = 1 
while su < 11:
    print("{}번" .format(su))
    su+=1
print("-" * 50)

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number : """

number = 0 
while number != 4 :
    print(prompt)
    number = int(input())
    
print("수고하셨습니다.")

