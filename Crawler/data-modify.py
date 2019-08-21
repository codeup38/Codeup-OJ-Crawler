#
#
#
#
#
#
#

def main():

    file = open("raw_data.txt", 'r+')    

    while True:
        text = file.readline()

        if not text:
            break

        #
        #   파싱한 뒤 제출 결과의 공백 제거
        #   구현 필요
    file.close()
    
if __name__ == 'main':
    main()
