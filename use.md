### 이용 방법

---------------------------------

**Windows 환경 기준으로 설명드립니다.**  

1. 파이썬3을 설치합니다.  
   <https://python.org/downloads> 에서 설치하실수 있으며, 저는 Python 3.7.4에서 개발하였습니다.  
   <br>

2. IDLE 또는 .py 파일을 컴파일해 실행할수 있는 컴파일러를 설치합니다.  
   참고로 IDLE는 Python 3를 설치할 때 설치됩니다. 따로 설치할 필요가 없습니다.  
   <br>

3. Windows PowerShell을 열고 아래의 명령어를 입력합니다.  
   **PowerShell 창이 열린 뒤에 몇 초간 딜레이가 있을 수 있습니다.**  

     ``` pip install requests ```  

     ``` pip install bs4 ``` 

     ```pip install tqdm```  <br>

4. repo에 올려져 있는 Crawler 폴더 자체를 다운받습니다.<br>
   먄약 raw-data-modifier.exe의 원래 소스 코드가 필요하다면 raw-data-modifier 폴더를 참고하시면 됩니다.  
    <br>

5. Crawler.py를 실행합니다. **크롤링 시 상태바가 보여집니다. 하지만 쉘 같은 환경에서는 제대로 상태바가 보이지 않을 수 있으니, exe 형태로 실행하는 것을 추천드립니다(IDLE 기준으로 그냥 클릭해서 실행)**    
   <br>
   origin_data.txt와 raw_data.txt가 생깁니다.<br>  
   raw_data.txt에서 빠진 제출번호는 없는지, 누락된 데이터는 없는지 확인해주세요.  <br>
   <br>
   origin_data는 제출 결과에 공백이 있고, raw_data는 공백이 없습니다.  <br>
   **이후 데이터 가공에 쓰이는 파일은 raw_data.txt입니다.**<br>
   <br><br>

6. raw_data_modifier.exe를 실행합니다.<br><br>

7. 프로그램의 실행이 끝나면 Rank LIst 폴더 내부에 4가지의 txt 파일이 생성됩니다.
   <br>
   각각의 txt 파일 내에 산출된 순위가 있습니다. ([참고](https://codeup.tk/how-to-rank))

   

   Enjoy :)

<br>

​	**Crawler.py의 사용을 권장하지 않습니다. 많은 사람이 해당 크롤러를 무분별하게 이용하여 Codeup OJ 서버에 과부화를 가하는 것을 원하지 않습니다.** 



**소스를 열람하며 열심히 익히고 응용하되, Codeup OJ의 운영자를 비롯한 다른 사람들을 위해 삼가해 주셨으면 합니다.**

<head>{% include Analytics.html %}</head>
