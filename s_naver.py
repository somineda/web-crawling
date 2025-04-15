from selenium import webdriver
from selenium.webdriver.chrome.options import Options #크롬에 옵션 설정
from bs4 import BeautifulSoup
import time #파이썬 개본 패키지

keyword = input("검색을 원하는 키워드를 입력해주세요:")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
options_ = Options() 
options_.add_argument(f"User-Agent={header_user}")
options_.add_experimental_option("detach",True) #자동으로 브라우저가 종료되지 않음

driver = webdriver.Chrome(options=options_) #크롬브라우저 사용을 위한 세팅을 자동으로 진행
driver.get(url)
time.sleep(1) 

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1) #로딩이 돼서 들어오는 시간안에 반복문이 안끝나게 1초마다 스크롤이 내려가도록 없을 시 그냥 맨 끝으로 실행됨

html = driver.page_source
soup =BeautifulSoup(html, "html.parser")
result = soup.select(".view_wrap")  #select/find -> select로 찾아서 나오는 결과는 리스트와 동일한 형태다

rank = 1
for i in result: 
    ad = i.select_one(".link_ad") #값이 있어 -> True / False / 챌린지 힌트
    
    if not ad :
        title = i.select_one(".title_link").text
        link = i.select_one(".title_link")["href"]
        writer = i.select_one(".name").text #작성자
        dsc = i.select_one(".dsc_link").text #요약 내용
        print(f"번호 : {rank}")
        print(f"제목 : {title}")
        print(f"링크 : {link}")
        print(f"작성자 : {writer}")
        print(f"글요약 : {dsc}")
        print('---------------')
        rank += 1