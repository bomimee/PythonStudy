import pandas as pd

e_list = [[100,"이도", "CEO"],
          [110,"마루치", "IT_PROG"],
          [121,"홍길동", "IT_PROG"],
          [227,"둘리", "IT_PROG"],
          [247,"공실이", "MANAGE"],
          ]
s_name = ["empno", "name", "job_id"]

df = pd.DataFrame(e_list, columns=s_name)
print(df)
print("-"*50)

#print(df[df["empno"]]>= 120)
print(df.query('empno>=120 and job_id == "IT_PROG"'))