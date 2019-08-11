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

def lastSubmit():

    user_agent = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    
    getreq = requests.get('https://codeup.kr/status.php', headers = user_agent)
    gethtml = getreq.text
    result = BeautifulSoup(gethtml, "html.parser")

    new_submit = result.select (
        'tr > td'
        )

    return new_submit[0].text

def main():

    user_agent = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    newSubmit = input(' 가장 최근에 제출된 제출 번호를 알고 싶다면 \
1을 입력하세요.\n 원하지 않으면 0을 입력해주세요.\n: ')
    
    if newSubmit=='1':
        print(lastSubmit()+'번 입니다.')

                              
    start = input(' 크롤링할 첫 제출 번호를 입력하시오 \n: ')
    end = input(' 크롤링할 마지막 제출 번호를 입력하시오\n: ') # 예외 case 작업 안함

    
    
    file = open("raw_data.txt",'w+')
    
    url = end
    start=eval(start)-1
    
    
    while True:
        
        req = requests.get('https://codeup.kr/status.php?&top='+url, headers = user_agent)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")

        inturl = eval(url)
        
        codeup_parser = soup.select (
            'tr > td'
            )

        
        for i in range (0,179,1):

            
            if (i%9==0) and (codeup_parser[i].text==str(start)):
                print('==========Done!==========')
                return 0

            if i%9==0 and i!=0:
                file.write('\n')
                
            file.write(codeup_parser[i].text)
            file.write(' ')

            
        

        file.write('\n')
        inturl-=20
        url = str(inturl)

    file.close()

    

if __name__ == '__main__':
    main()
