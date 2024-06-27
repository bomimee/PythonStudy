import pandas as pd

df = pd.read_csv('day10/data/test_data.tsv')
print(df)
print(type(df))
print(df.head()) #상위5개
print(df.tail()) #하위5개
