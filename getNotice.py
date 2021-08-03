import configparser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date

#코로나공지
coronaNotice = "https://www.mju.ac.kr/mjukr/3860/subview.do"
#학사공지
academicNotice = "https://www.mju.ac.kr/mjukr/257/subview.do"
#일반공지
generalNotice = "https://www.mju.ac.kr/mjukr/255/subview.do"
#장학금공지
scholarshipNotice = "https://www.mju.ac.kr/mjukr/259/subview.do"
#취업공지
careerNotice = "https://www.mju.ac.kr/mjukr/260/subview.do"

noticeURL = [coronaNotice, academicNotice, generalNotice, scholarshipNotice, careerNotice]
noticeName = ["코로나19종합공지", '학사공지', '일반공지', '장학금공지', '취업공지']

today = date.today().isoformat()

# config.ini 파일에 경로 작성
config = configparser.ConfigParser()
config.read('./config.ini')
storage_path = config['STORAGE']['STORAGE_PATH']

#파일 이름 설정
fileName = storage_path + today + "공지사항.txt"

f = open(fileName, 'w')

for idx in range(5):
    response = urlopen(noticeURL[idx])
    f.write(noticeName[idx] + '\n')
    soup = BeautifulSoup(response, 'html.parser')
    newArtcl = soup.select("span.newArtcl")
    if len(newArtcl) == 0:
        f.write("새로운 공지 없음." + "\n")
    else:
        for icon in newArtcl:
            a = icon.parent
            contents = a.contents
            f.write(contents[1].get_text() + '\n')
            link = "https://www.mju.ac.kr" + a.get('href')
            f.write(link + '\n')
    f.write("\n")
f.close()



