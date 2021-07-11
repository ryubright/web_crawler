import chromedriver_autoinstaller
from web_crawler.utils.crawling_base import CrawlingBase

from web_crawler.tasks import NaverBlogCrawler, DaumBlogCrawler

TASKS = {
    "naver_blog": NaverBlogCrawler,
    "daum_blog": DaumBlogCrawler
}

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
base_driver_path = f'./{chrome_ver}/chromedriver.exe'


class WebCrawler:
    def __new__(
            cls,
            task: str,
            keyword: str,
            max_page_no: int,
            driver_path: str = base_driver_path,
    ) -> CrawlingBase:
        if task not in TASKS:
            raise KeyError("정의 되지 않은 task입니다.")

        crawling_object = TASKS[task](keyword, max_page_no, driver_path)

        return crawling_object


task = input('select task('
             'naver_blog, '
             'daum_blog) : ')
keyword = input('키워드를 입력하세요 : ')
max_page_no = int(input('페이지수를 입력하세요. : '))

web_crawler = WebCrawler(task, keyword, max_page_no)
web_crawler()
