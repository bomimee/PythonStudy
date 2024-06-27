# numpy 모듈 : 대규모, 다차원 배열을 다루기 위한 외부 모듈
#              기본적으로 array라는 자료형을 사용함 (행렬의 개념과 비슷함)  
#              아나콘다 설치시 함께 설치됨, (개인적으로 설치 시 터미널에 pip install numpy ) 
#              import numpy as np 호출
#              리스트 자료형과 아주 유사함(인덱싱과 슬라이싱)

import numpy as np



# 1차원 배열 다루기  :  numpy array([한가지 종류가 저장된 리스트])
#                     리스틀 배열로 바꾸어서 사용함
# 배열변수 = np.array([list])
# 배열변수 : 할당된 배열공간의 주소를 참조하는 레퍼런스 변수임(주소저장변수)
# 배열로 만들 리스트는 반드시 정수 | 실수 값들로만 구성되어 있어야 한다.
'''
    리스트 : -, / 연산 불가능
             + 연결,  * 반복연산
    배열 : 사칙연산 모두 가능
'''



ar = np.array([0,1,2,3,4,5,6,7,8,9])
# numpy.ndarray 는 다차원 배열 구조 => 선형대수 계산에 이용
print(ar, type(ar))
print("-" * 50)

ar = np.array([0.0, 1.0,2.0,3.0,4.0,5.0])
print(ar, type(ar))
print("-" * 50)

ar = np.array([0.9, 1 ,2.4 ,3.3 ,4, 5.0])
print(ar, type(ar))
print("-" * 50)

# 자료형을 하나로 통일 시킨다.(모두가 string이 된다.)
ar = np.array(['a', 'r', "body", 1, 3.4])
print(ar, type(ar))
print("-" * 50)

# 스칼라 : 크기만 가지고 방향은 가지고 있지 않은 양,   a = 24 
# 백터   : 크기와 방향을 가지고 있는 양 ,  배열(numpy의 array)

# 리스트일때 벡터화(배열) 연산 처리의 예
datalist = [0,1,2,3,4,5,6,7,8,9]

# 리스트 요소를 2배로 증가 하자
for i in datalist:
    datalist[i] = i * 2
    
print(datalist)

# 리스트를 배열로 만들어서 각 요소를 2배로 증가하자.
datalist2 = [0,1,2,3,4,5,6,7,8,9]
ar = np.array(datalist2)
print(ar * 2 )

# 만약에 리스트를 배열처러 사용하면 각 요소가 2배로 증가하지 않고 
print(datalist2 * 2)
print("-" * 50) 

a = [1,2,3,4,5]
b = np.array(a)

# 리스트와 배열 연산의 차이
print(a+a) # 반복 
print(b+b) # 실제 계산 

print(a*2) # 반복 
print(b*2) # 실제 계산 
print("-" * 50) 

# 배열은 비교연산, 논리연산, 산술연산이 가능
ar1 = np.array([1,2,3])
br1 = np.array([10,20,30])

print(2 * ar1 + br1)         # 2*ar[0]+br[0] = 12, 
print(ar1 == 2)              # [False True False]
print(br1 == 2)              # [False False False]
print(ar1 >= 2)              # [False True True]
print((ar1 == 2) & (br1 >10)) # ar1[0]==2(F) & br1[0]>10(F) => False





