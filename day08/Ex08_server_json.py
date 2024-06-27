from urllib.request import urlopen
from urllib.parse import urlencode
import json


url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={
    'serviceKey' : '7Jn37duPnqJP2hXtNvhcywuZlcu2XWgEJYHRSJIIwWps7J94qVJ8gOWdJOJSqoQ9rH2YQCMaCFMtlFsxFPAv8A==', 
    'returnType' : 'json', 
    'numOfRows' : '100', 
    'pageNo' : '1', 
    'sidoName' : '서울', 
    'ver' : '1.0' }

query_string = urlencode(params)

# 파이썬의 f-string을 사용하여 문자열을 조립하는 방식
# f"{url}?{query_string}"은 url과 query_string을 합쳐서 하나의 완전한 URL을 형성
myurl = f"{url}?{query_string}"

response = urlopen(myurl)
data = json.load(response)
# print(data)

# 딕셔너리 하나
# print(type(data) , len(data))
list = data["response"]["body"]["items"]   
for i in list:
    print(i["sidoName"], end="   ")
    print(i["stationName"], end="   ")
    print(i["pm10Value"], end="   ")
    print(i["pm25Value"])


