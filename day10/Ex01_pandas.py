import pandas as pd
import numpy as np

np.random.seed(101) #같은 시드값지정하면 같은 랜던값이 나온다
data = np.random.randn(5,4)
df = pd.DataFrame(data, columns=['W', 'X', 'Y', 'Z'], index=['A', 'B','C','D','E'])
print(df)

print(df.info)
print("-"*50)
#데이터 프레임 인덱싱 / 슬라이싱 
print(df['W'])
#print(df[1]) #인덱스 사용못함
print(df[['W','Z']], type(df[['W','Z']]))
df['new'] = df['W'] + df['X']
print(df)

#컬럼삭제
print(df.drop('new',axis=1)) #원본삭제안됨
print(df)
print(df.drop('new',axis=1, inplace = True)) #원본삭제
print(df)

df2 = pd.DataFrame({'A':[1,2, np.nan],
                    'B':[5,np.nan, np.nan],
                    'C':[1,2, 3],
                    })
print(df2)
m_cnt = df2.isnull().sum()   #NAN갯수 구하기
print("각열의 결측치 개수: {}" .format(m_cnt))

# 결측치를 포함하고 있는 모든 행 삭제  = dropna()
print(df2.dropna())
