# 딕셔너리 입/출력

import csv

with open("day04/data/csv03.csv","w", encoding="utf-8", newline="") as f1:
    #wr = csv.writer(f1)
    fname =["name", "age", "addr"]  # 키값
    wr = csv.DictWriter(f1, fieldnames=fname)
    wr.writeheader()  # 키값 => 컬럼명
    wr.writerow({"name" : "hong", "age" : "24", "addr":"서울"})
    wr.writerow({"name" : "kang", "age" : "14", "addr":"경기"})
    wr.writerow({"name" : "park", "age" : "21", "addr":"제주"})
    
with open("day04/data/csv03.csv","r", encoding="utf-8") as f2:
    # rd = csv.reader(f2)
    rd = csv.DictReader(f2)
    for i in rd:
        #print(i)
        print(i["name"], i["age"], i["addr"])

# 성년 미성년 추가 하기 
