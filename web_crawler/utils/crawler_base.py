import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from abc import abstractmethod


class CrawlerBase(object):
    def __init__(
            self,
            keyword: str,
            max_page_no: int,
            driver_path: str,
            ip_bypass_flag: bool
    ):
        self.keyword = keyword
        self.max_page_no = max_page_no
        self.error_count = 0
        self.count = 0

        if not ip_bypass_flag:
            self.options = Options()
        else:
            for i in range(3):
                self.options = self._set_ip_bypass()

        try:
            self._driver = webdriver.Chrome(f"{driver_path}", options=self.options)
        except:
            chromedriver_autoinstaller.install(True)
            self._driver = webdriver.Chrome(f"{driver_path}", options=self.options)

        self.main_url, self.sub_url = self.get_url

    def _set_ip_bypass(self):
        options = Options()

        options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument(
            "app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36")

        return options

    @abstractmethod
    def get_url(self) -> str:
        raise NotImplementedError(
            "`get_url()` is not implemented properly!")

    @abstractmethod
    def _crawling(self) -> list:
        raise NotImplementedError(
            "`crawling()` is not implemented properly!")

    @abstractmethod
    def _to_csv(self) -> None:
        raise NotImplementedError(
            "`to_csv()` is not implemented properly!")
