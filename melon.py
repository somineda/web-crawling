import requests 
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser") #파이썬도 html을 어느정도 파악 가넝

#lst50/ lst100
lst50 = soup.select(".lst50") #list
lst100 = soup.select(".lst100")
add_list =  lst50 + lst100

for rank, i in enumerate(add_list, 1): #증가하는 숫자를 자동으로 만들어 줌->rank에 저장 
    title = i.select_one(".ellipsis.rank01 a").text #클래스명이 두개일 때 공백을 지우고 각각의 클래스명 앞에 . 찍기
    singer = i.select_one(".checkEllipsis").text
    album = i.select_one(".ellipsis.rank03 a").text

    print(f"[순위] : {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] : {singer}")
    print(f"[앨범] : {album}")
    print("---"*20)