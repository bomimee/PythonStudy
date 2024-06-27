
import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구데이터

city = pd.Series([9857426, 2475231, 3454958, 2938484], index=["서울", "대전", "대구", "부산"])

#in : 주로 검색 용도로 사용
print("서울" in city) # True
print("수원" in city) #False

for k,v in city.items():
  print("{0} = {1}" .format(k,v))

print("---------------------딕셔너리 객체에서 시리즈 생성")
dic = {"서울":10020221 , "대전":2939459, "대구":29394857, "부산":2938750}
city2 = pd.Series(dic)
print(city2)

print("--인덱스 기반의 연산 --")
res = city - city2
print(res)

print("--인덱스 기반의 연산 --")
res2 = city.values -city2.values
print(res2)
#딕셔너리는 순서가 없다. 순서를 주려면 인덱스 사용
dic2 = {"서울":10020221 , "대전":2939459, "대구":29394857, "부산":2938750, "인천" : 2847596}
city3 = pd.Series(dic2)
res3 = city -city3

print(res3)
print(res3.notnull()) #데이터가 없으면 F

print(res3[res3.notnull()])

print("--인덱스 기반의 연산 계산 추가 삭제-")
city2["부산"] = 7777984
print(city2)
city2["광주"] = 7777984
print(city2)
