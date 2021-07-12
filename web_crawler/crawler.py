import chromedriver_autoinstaller

from web_crawler.utils.crawling_base import CrawlingBase
from web_crawler.tasks import NaverBlogCrawler, DaumBlogCrawler

TASKS = {
    "naver_blog": NaverBlogCrawler,
    "daum_blog": DaumBlogCrawler
}

CHROME_VER = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
BASE_DRIVER_PATH = f'./{CHROME_VER}/chromedriver.exe'


class WebCrawler:
    def __new__(
            cls,
            task: str,
            keyword: str,
            max_page_no: int,
            driver_path: str = BASE_DRIVER_PATH,
    ) -> CrawlingBase:
        if task not in TASKS:
            raise KeyError("정의 되지 않은 task입니다.")

        crawling_object = TASKS[task](keyword, max_page_no, driver_path)

        return crawling_object
