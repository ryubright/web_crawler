# web_crawer

- 웹페이지의 텍스트 데이터를 수집하기 위한 서비스입니다.
- 현재 네이버 블로그, 다음 블로그 크롤러가 구현됐습니다.
- 네이버 블로그는 제목, 요약된 본문을 수집하고 다음 블로그는 제목, 본문 전체를 수집합니다.

<br>

## requirements
- selenium : _pip install selenium_
- pandas : _pip install pandas_
- chromedriver-autoinstaller : _pip install chromedriver-autoinstaller_
<br>

## 사용법
__blog_crawling.py__ 파일을 실행합니다.

<br>

![image](https://user-images.githubusercontent.com/59256704/125160896-4d2ea000-e1ba-11eb-883f-521c9f8a7753.png)

크롤링을 원하는 웹페이지의 종류를 입력합니다.

<br>

![image](https://user-images.githubusercontent.com/59256704/125160902-50c22700-e1ba-11eb-8135-62d7d104a883.png)

원하는 keyword, page수를 입력합니다.

<br>

![image](https://user-images.githubusercontent.com/59256704/125160907-51f35400-e1ba-11eb-92af-6778b57eb426.png)

크롤링이 완료가 되면 .csv파일이 생성되고, 결과를 출력합니다.
