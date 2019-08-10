# Codeup OJ Status Crawler
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

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
    start = input('크롤링할 첫 제출 번호를 입력하시오 : ')
    end = input('크롤링할 마지막  제출 번호를 입력하시오 : ') # 예외 case 작업 안함

    url = end

    #num = eval(end)-eval(start)
    
    while True:
        
        req = requests.get('https://codeup.kr/status.php?&top='+url)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")

        inturl = eval(url)
        
        codeup_parser = soup.select (
            'tr > td'
            )

        
        for i in range (0,179,1):

            #print(i)
            
            if (i%9==0) and (codeup_parser[i].text==start):
                
                return 0

            if i%9==0 and i!=0:
                print('')
                
            print(codeup_parser[i].text, end=' ')

            
        

        print('')
        inturl-=20
        url = str(inturl)

if __name__ == '__main__':
    main()
