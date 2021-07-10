import chromedriver_autoinstaller
from selenium import webdriver
from abc import abstractmethod


class CrawlingBase(object):
    def __init__(
            self,
            keyword: str,
            max_page_no: int,
            driver_path: str
    ):
        self.keyword = keyword
        self.max_page_no = max_page_no
        self.error_count = 0

        try:
            self._driver = webdriver.Chrome(f"{driver_path}")
        except:
            chromedriver_autoinstaller.install(True)
            self._driver = webdriver.Chrome(f"{driver_path}")

        self.main_url, self.sub_url = self.get_url

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
