# Codeup OJ Status Crawler
# 
# 
#
# Copyright 2019 kimgihong38 All rights reserved.
# https://codeup.kr/userinfo.php?user=kimgihong38
#
#
# 콘텐츠를 허가 없이 크롤링하여 사용하는 것은 불법입니다.
#
# 해당 Crawler Source Code를 활용하여 특정 사이트 크롤링을 하기 전에
# 특정 사이트 운영자에게 허락을 구하고 크롤링 진행을 하기 바랍니다.
#
#

import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

from Submit-Crawler import lastSubmit

# Status page : 20 user
# 9 info; tr > td option
# 0 Submit Num
# 1 ID
# 2 prob ID
# 3 res
# 4 memory
# 5 Time
# 6 lang
# 7 len
# 8 Time


def main():

    user_agent = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    start = None
    end = None
    print('날짜 입력이 형식에 맞지 않거나, 잘못 입력할 경우에는 다시 입력 \
하도록 설정되어 있습니다.\n주의해주세요.','')
    
    while not bool(re.match('201\d-[01]\d-[0123]\d',start)):            
        start = input(' 크롤링할 제출 기록 시작 날짜(YYYY-MM-DD)\n: ')

    while not bool(re.match('201\d-[01]\d-[0123]\d',end)):
        end = input(' 크롤링할 제출 기록 종료 날짜(YYYY-MM-DD)\n: ') 

        
    url = lastSubmit()
    
    
    while True:
        
        req = requests.get('https://codeup.kr/status.php?&top='+url, headers = user_agent)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")

        inturl = eval(url)
        
        codeup_parser = soup.select (
            'tr > td'
            )
# 아직 구현 삽질중..
        
        for i in range (0,179,1):

            
            if (i%9==0) and (codeup_parser[i].text==str(start)):
                print('==========Done!==========')
                return 0

            if i%9==0 and i!=0:
                file.write('\n')
                
            file.write(codeup_parser[i].text)

            
        

        file.write('\n')
        inturl-=20
        url = str(inturl)





if __name__ == '__main__':
    main()
