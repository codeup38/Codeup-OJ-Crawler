# Codeup OJ Status Crawler
# 시작 날짜-종료 날짜 구현은 이후로 미룸
# 우선 제출 번호 기준으로 
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
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://codeup.kr/status.php")
bsObject = BeautifulSoup(html, "html.parser")


for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))




def inputstartday(): # 시작 날짜 입력 함수
    startDay = input('크롤링할 제출 기록 시작 날짜(YYYY-MM-DD) : ')

    start=bool(re.match('201\d-[01]\d-[0123]\d',startDay))

    if not start:
        print('입력된 날짜를 다시 확인해주세요.\n')
        inputstartday()
    else:
        return startDay


def inputendday(): # 종료 날짜 입력 함수
    endDay = input('크롤링할 제출 기록 종료 날짜(YYYY-MM-DD) : ')

    end=bool(re.match('201\d-[01]\d-[0123]\d',endDay))

    if not end:
        print('입력된 날짜를 다시 확인해주세요.\n')
        inputendday()
    else:
        return endDay



def main():
    print('Codeup Status Crawler')
    print('================================')
    print('')
    print('')

    
    print('제출 일자를 기준으로 크롤링합니다.\n')
    print('원하시는 날짜를 기입해주세요.\n')

    startDay=inputstartday()
    endDay=inputendday()

    #input 버그를 해결했다고 가정합시다..ㅠㅠㅠ
    

if __name__ == '__main__':
    main()
                             
