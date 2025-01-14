import pandas as pd

emp_list = [{"empno":100, "name":"이도", "job_id":"CEO"},
             {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
             {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":121, "name":"홍길동", "job_id":"Sales"},
             {"empno":210, "name":"마루치", "job_id":"IT_PROG"},
            {"empno":227, "name":"일지매", "job_id":"IT_PROG"},
            {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":255, "name":"마이클", "job_id":"Sales"},
             {"empno":236, "name":"아수라", "job_id":"Analysis"},
            {"empno":270, "name":"어두일미", "job_id":"Analysis"},
            {"empno":282, "name":"을불", "job_id":"IT_PROG"}]

df = pd.DataFrame(emp_list)

#중복된 행 찾아 삭제하기
res = df.duplicated()
print(res)

res2 = df.drop_duplicates()
print(res2)

#이름이 같은 데이터 찾아서 삭제하기
res3 = df.drop_duplicates(["name"])
print(res3)