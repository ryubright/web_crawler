import chromedriver_autoinstaller
from web_crawling.tasks.naver_blog import NaverBlogCrawler
from web_crawling.tasks.daum_blog import DaumBlogCrawler


keyword = input('키워드를 입력하세요 : ')
max_page_no = int(input('페이지수를 입력하세요. : '))

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

daum_blog_crawler = DaumBlogCrawler(keyword, max_page_no, f'./{chrome_ver}/chromedriver.exe')
daum_blog_crawler()

naver_blog_crawler = NaverBlogCrawler(keyword, max_page_no, f'./{chrome_ver}/chromedriver.exe')
naver_blog_crawler()