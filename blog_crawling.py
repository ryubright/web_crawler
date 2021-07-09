from web_crawling.naver_blog.naver_blog_crawling import BlogCrawler

keyword = input('키워드를 입력하세요 :')
page_no = int(input('페이지수를 입력하세요. (한 페이지에 총 7개의 블로그에 대한 정보가 담겨있습니다) :'))

blog_crawler = BlogCrawler(keyword, page_no, 'chromedriver.exe')
blog_crawler()
