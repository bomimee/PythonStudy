#시계열 데이터(시리즈 = numpy 1차원) 나 데이터프레임(table = numpy 2차원 행렬)

import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구데이터

city = pd.Series([9857426, 2475231, 3454958, 2938484], index=["서울", "대전", "대구", "부산"])
div = city / 1000000

print(div)

print(city[1], city["대전"])
print(city[3], city["부산"])

print(city[[1,3,0]])
print(city[["대전", "부산", "서울"]])

x = pd.Series(range(3), index=["a", "b", "다"])
print(x)

print(x.a)
print(x.b)
print(x.다)