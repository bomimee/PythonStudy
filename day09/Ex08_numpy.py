import numpy as np

#브로드캐스팅
#백터(행렬)끼리 덧셈 또는 뺄셈을 하려면, 행과 열의 갯수가 같아야 함(원칙)
#numpy 에서 행과 열이 다른 벡터끼리도 연산이 가능하도록 지원 => 브로드캐스팅
#크기가 작은 벡터가 자동으로 크기가 큰 벡터의 행과 열 갯수와 맞춰짐(확장)

x = np.arange(5)
print(x)

y = np.ones_like(x)
print(y)
print("-"*50)
print( x+y)
print(x+1)

print(x+y)
print(x+5)

#배열연결 : 두 개이상의 배열들을 연결해서 하나의 큰 배열을 만듦
#      hstack, vstack, dstack
# hstack(horizontal stack)
ar1 = np.ones((2,3))
print(ar1)

ar2 = np.zeros((2,2))
print(ar2)

print(np.hstack([ar1,ar2]))
print("-"*50)
#vstack: 열의 갯수가 같은 1차원 배열들을 위 아래로 (새로) 합칠때 사용 => 행 갯수가 늘어나게됨

ar3 = np.ones((2,3))
print(ar3)

ar4 = np.zeros((3,3))
print(ar4)

print(np.vstack([ar3,ar4]))
print("-"*50)
#dstack(depth stack) : depth = 면 (차원)
#                     1차원 배열 여러 개를 깊이 방향으로 합칠때 사용
#                     a행 * b 열일때 배열의 갯수가 n개 합치면, 결과는 a 면 * b행 * n열이 된다.
ar5 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(ar5)

ar6 = np.array([[5,6,7,8],[9,10,11,12],[1,2,3,4]])
print(ar6)

ar7 = np.dstack([ar5, ar6])
print(ar7)
print(ar7.shape)

ar8 =np.stack([ar5, ar6])
print(ar8)
print(ar8.reshape)
print("_"*50)

print(np.random.seed(5))
print(np.random.rand(5))

#데이터 섞기
x = np.arange(10)
print(x)

