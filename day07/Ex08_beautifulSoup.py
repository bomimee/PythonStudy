# 네이버 웹툰 정보 가져오기 (크롤링)
# https://comic.naver.com/webtoon/weekday
# https://comic.naver.com/webtoon?tab=wed

from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "https://ictedu.co.kr/index.php?main_page=home"
response = urlopen(myurl)

soup = BeautifulSoup(response,"html.parser")
#print(soup)

c_title = soup.find_all("h3", {"class" : "title"})

for i in c_title:
  print(i.find("a").string)  #string = getText

c_lt = soup.find_all("li", {"class" : "lt"})
for i in c_lt:
  print(i.find("div").string)
  
  #두개를 포함하고 있는 요소 찾기
c_info = soup.find_all("div", {"class":"info"})
for i in c_info:
  c_title = i.find("h3", {"class":"title"}).find("a").string.strip()
  print(c_title)
  c_lt = i.find("li", {"class":"lt"}).find("div").string.strip()
  print(c_lt)
  print("-"*50) 