from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={
    'serviceKey' : '7Jn37duPnqJP2hXtNvhcywuZlcu2XWgEJYHRSJIIwWps7J94qVJ8gOWdJOJSqoQ9rH2YQCMaCFMtlFsxFPAv8A==', 
    'returnType' : 'xml', 
    'numOfRows' : '100', 
    'pageNo' : '1', 
    'sidoName' : '서울', 
    'ver' : '1.0' }

response = requests.get(url, params=params)
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

        # find_all = select = 여러개 
c_item = soup.find_all("item")
for i in c_item:
    # find = select_one  => 하나찾기
    # get_text() = string => 태그글자 추출
    print(i.select_one("sidoName").string, end = "   ")
    #print(i.find("sidoname"))
    print(i.select_one("stationName").string, end = "   ")
    print(i.select_one("pm10Value").string, end = "   ")
    print(i.select_one("pm25Value").string)