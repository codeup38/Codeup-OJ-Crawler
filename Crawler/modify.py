#
#
#
#
#
#
#

def modifyData():

    
    file = open("data_origin.txt", 'r')    
    printFile = open("raw_data.txt",'w+')
    

    while True:
        text = file.readline()
        res = text.split()

        
        if not text:
            break
            
        
        if res[3] == '실행' or res[3] == '출력': # 실행 중 에러 or 출력 한계 초과
            for i in range(len(res)-2):
                if i == 3:
                    printFile.write(res[3]+res[4]+res[5])
                    printFile.write(' ')
                elif i < 3:
                    printFile.write(res[i])
                    printFile.write(' ')
                else:
                    printFile.write(res[i+2])
                    printFile.write(' ')
                
            printFile.write('\n')

        elif res[3] == '컴파일' and res[4] == '중': # 컴파일 중 ---
            print('데이터 내에 \'컴파일 중\'인 데이터가 있습니다.\n')
            print(res[0],'번을 확인해주세요. (크롤링에서 제외됩니다)\n')

        else:
            for i in range(len(res)-1):
                if i == 3:
                    printFile.write(res[3]+res[4])
                    printFile.write(' ')
                elif i < 3:
                    printFile.write(res[i])
                    printFile.write(' ')
                else:
                    printFile.write(res[i+1]) 
                    printFile.write(' ')
        
            printFile.write('\n')

                
        
        
    file.close()
    printFile.close()
    
    
if __name__ == '__main__':
    modifyData()
    print('Done!')
    input('Press Any Key ')
