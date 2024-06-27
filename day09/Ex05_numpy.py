import numpy as np 

# zeros : 크기가 정해진 모든 값이 0인 배열 생성
z_ar = np.zeros(5)
print(z_ar, type(z_ar), z_ar.dtype)

z_ar2 = np.zeros((2,3))
print(z_ar2)

# 크기를 지정하지않고 다른 배열의 크기를 차용해서 만든다.
one_ar = np.ones_like(z_ar)
print(one_ar)

one_ar2 = np.ones_like(z_ar2)
print(one_ar2)
print("-" * 50)

arr = np.arange(10)
print(arr) 

arr2 = np.arange(3,21,3)   #(시작,끝, 간격)
print(arr2)
print("=" * 5)

ls = np.linspace(0,100,1)  #(시작,끝,개수)
print(ls)

ls = np.linspace(0,100,2)  #(시작,끝,개수)
print(ls)

# 균일하게 간격을 둔 5개의 수사즐 생성
ls = np.linspace(0,100,5)  #(시작,끝,개수)
print(ls)
