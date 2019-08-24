# Codeup OJ Tier Service
#### Powered by Codeup OJ Crawler (ver. 1.0.0)

<br>
repo 주소 : [Codeup-OJ-Crawler](https://github.com/codeup38/Codeup-OJ-Crawler/blob/master/index.md)    

랭킹 산출 기준 : [how-to-rank](https://codeup.tk/how-to-rank)

코드업 주간 제출현황 분석 보러가기 : [MoonWalk - Prestige WorkSpace](https://blog.creatively.dev/tags/#%EC%A3%BC%EA%B0%84%20%EC%BD%94%EB%93%9C%EC%97%85%20%EB%9E%AD%ED%82%B9)

-----------------------------------------

안녕하세요. Codeup OJ Crawler 개발자 codeup38입니다.  (~~이제 당당하게 개발자라고 할수 있습니다 ㅎㅎ~~)

코드업에서는 [ID) kimgihong38](https://codeup.kr/userinfo.php?user=kimgihong38) 을 사용하고 있습니다.  

<br>
가장 메인 모듈인 Crawler.py 파일에 주석으로 쓴 내용처럼  <br>
타인의 사이트를 허가받지 않고 크롤링하는 행위는 **차후에 문제가 될 수 있으며**  

기본적으로 제 Codeup-OJ-Crawler repo는 MIT license이기 때문에 자유롭게 이용, 활용하셔도 상관은 없으나  <br>
**사이트의 운영자에게 허락을 구하는 것이 먼저입니다.**
<br>

예를 들어, [Codeup OJ](https://codeup.kr)같은 사이트에서 사용하시려면 사이트의 운영자인 [admin](https://codeup.kr/userinfo.php?user=admin)님에게 허락을 구하는 것이 먼저입니다.  
<br>
**실제로 저는 admin님에게 직접 사용 용도와 서버에 미칠 영향 등을 설명드리고 허락을 구했고, 허락을 받았습니다.**

<br>
이 점 유념해 주셨으면 좋겠습니다.
<br>
저처럼 C/C++만 공부하다 웹 크롤링에 관심이 생겨, 파이썬을 조금이나마 공부해보고, 실제로 웹 크롤러를 구현해보고 싶으신 분들에게  
제 소스가 많은 도움이 되었으면 합니다.  

<br>
저 또한 굉장히 고생했으니까요..(~~하지만 아직 고생할게 너무 많이 남았죠~~)  
아래는 이용 방법입니다. 참고하세요.

--------------------------------

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

​	**Crawler.py의 사용을 권장하지 않습니다. 많은 사람이 해당 크롤러를 단순히 이용하여 Codeup OJ 서버에 과부화를 가하는 것을 원하지 않습니다.** 



**소스를 열람하며 열심히 익히고 응용하되, Codeup OJ의 운영자를 비롯한 다른 사람들을 위해 삼가해 주셨으면 합니다.**
