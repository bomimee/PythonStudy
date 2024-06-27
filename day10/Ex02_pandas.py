import pandas as pd
import numpy as np

m_dict = [{'id':1010, 'name':'마루치', 'Java':89, 'Python':78, 'Flask':90},
          {'id':1230, 'name':'아라치', 'Java':96, 'Python':80, 'Flask':92},
          {'id':1902, 'name':'을불', 'Java':90, 'Python':74, 'Flask':90},
          {'id':2002, 'name':'창조리', 'Java':98, 'Python':88, 'Flask':94}]

data = pd.DataFrame(m_dict)
print(data)

data['sum'] = data['Java']+data['Python']+data['Flask']
print(data)
data['average'] = np.around(data['sum'] / 3)
print(data)

print('학점은 리스트에 담아서 나중에 추가하자')
grade = []
for i in data['average']:
  if i>=90:
    grade.append('A')
  elif i>=80:
    grade.append('B')
  elif i>=70:
    grade.append('C')
  else:
    grade.append('F')
data["grade"]  = grade
print(data)          