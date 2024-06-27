from urllib.request import urlopen
from bs4 import BeautifulSoup

#myurl = "http://www.kma.go.kr/XML/weather/sfc_web_map.xml"
#soup = BeautifulSoup(response,"html.parser")
myurl = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
response = urlopen(myurl)

soup = BeautifulSoup(response, "xml")

print(soup)
data_list = []
#도시, 날씨, 최저기온, 최고 기온을 파싱하시오.

for location in soup.find_all("location"):
    city = location.city.get_text()
    for data in location.find_all("data"):
    
        wf = data.find("wf").get_text()
        tmn = data.find("tmn").get_text()
        tmx = data.find("tmx").get_text()

        data_list.append({
            "city": city,
            "wf": wf,
            "tmn": tmn,
            "tmx": tmx
        })

for data in data_list:
    print(data)