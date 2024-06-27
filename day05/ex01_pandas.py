#pandas install

import pandas as pd

data= pd.read_excel('day05/data/excel02.xlsx')

#상위 데이터 확인 (5개)
print(data.head())
print("-"*50)

#하위 데이터 확인(5개)
print(data.tail())

print(data)
print("-"*50)

print(data.shape)
print("-"*50)

data.to_csv('')

