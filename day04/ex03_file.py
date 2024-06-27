'''
    파일 입/출력
    이름 = open('파일이름', 옵션)   
    -- 중간과정--
    이름.close()
    
    ** 옵션 
     - r 모드 : 읽기
     - w 모드 : 쓰기 (기존 파일이 있으면 덮어쓰기가 된다.,  없으면 새로 생성한다.) 
     - a 모드 : 추가
'''

# os는 Python의 표준 라이브러리, 운영체제와 상호 작용할때 사용하며, 다양한 운영 체제 관련 기능 제공
# 파일 및 디렉토리 관리, 파일 경로 관리,....

#import os

# 현재 위치 저장
# c_dir = os.path.dirname(__file__)
# print(c_dir)
# f_path =  os.path.join(c_dir+"/data", "text01.txt")

# f = open(f_path, 'w', encoding="utf-8")

# 터미널 위치
f = open("day04/data/text02.txt", 'w', encoding="utf-8")
for i in range(1,6):
    str1 = "{}번째 줄 ....\n" .format(i)
    f.write(str1)
f.close()
print('-' * 50)

f = open("day04/data/text01.txt", 'r', encoding="utf-8")
while True:
    line = f.readline()
    print(line)
    if not line : break
f.close()
print('-' * 50)

f = open("day04/data/text01.txt", 'r', encoding="utf-8")
lines = f.readlines()
# print(lines, type(lines)) # 리스트로 나옴 
for i in lines:
    print(i)
f.close()
print('-' * 50)

f = open("day04/data/text01.txt", 'r', encoding="utf-8")
data = f.read()
print(data, type(data)) # string로 나옴 
f.close()
print('-' * 50)
