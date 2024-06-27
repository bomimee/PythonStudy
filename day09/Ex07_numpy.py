import numpy as np

#배열간의 연산
#백터의 내적 : 두백터의 차원이 같아야한다.
#             각 요소의 곱을 모두 더한것이다.
#             dot 함수 사용 => 결과는 스칼라( 값이 나옴)
a = np.array([2,5,1])
print(a, type(a))


b = np.array([4,3,5])
print(b, type(b))

print(np.dot(a,b.T))

#matrix 곱셈
c = np.array([[2,1], [1,4]])
d = np.array([[1,2,3],[0,1,2]])
print(np.matmul(c,d))