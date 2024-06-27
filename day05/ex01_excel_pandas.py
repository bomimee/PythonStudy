# 판다스 설치 : pip install pandas

import pandas as pd

data = pd.read_excel('day05/data/excel02.xlsx')

# 상위 데이터 확인 (5개)
print(data.head())
print("-" * 50)

# 하위 데이터 확인 (5개)
print(data.tail())
print("-" * 50)

print(data)
print("-" * 50)

# 전체 행과 열의 갯수
print(data.shape)  # (20, 7)
print("-" * 50)

data.to_csv('day05/data/excel_csv.csv')
# 인덱스 번호 사용 안함
data.to_csv('day05/data/excel_csv2.csv', index=False)

data.to_excel('day05/data/excel_xl.xlsx', index=False)