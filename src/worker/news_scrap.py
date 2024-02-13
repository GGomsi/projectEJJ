import requests
import json
from bs4 import BeautifulSoup
from create_folder import create_folder_with_today
import os

# 딕셔너리 리스트
dictList = []

response = requests.get("https://news.naver.com/main/ranking/popularDay.naver")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".list_content")

for link in links:
    News = link.contents[1]
    title = News.contents[0]
    url = News.attrs['href']
    # 현재 기사
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    curNews = soup.select("#dic_area")
    curNews = curNews[0]
    contents = curNews.text
    
    curDict = {'title': title, 'url': url, 'contents': contents}
    dictList.append(curDict)
    
# 오늘날짜 폴더 생성
folderPath = create_folder_with_today()
filePath = os.path.join(folderPath, f"TodayTopic.json")

# 리스트를 JSON 형식의 문자열로 변환
json_string = json.dumps(dictList, ensure_ascii=False)

# JSON 문자열을 파일로 저장
with open(filePath, 'w', encoding="utf-8") as json_file:
    json_file.write(json_string)