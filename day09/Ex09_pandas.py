#시계열 데이터(시리즈 = numpy 1차원) 나 데이터프레임(table = numpy 2차원 행렬)

import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구데이터

city = pd.Series([9857426, 2475231, 3454958]) 
print(city)
print("-"*50)
city2 = pd.Series([9857426, 2475231, 3454958, 2938484], index=["서울", "대전", "대구", "부산"])
print(city2, type(city2))
print("-"*50)
print(city2.index)
print(city2.values)
city2.name = "도시별 인구수"
print(city2)