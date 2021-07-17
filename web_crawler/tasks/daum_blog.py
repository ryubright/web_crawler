import pandas as pd
import random
from time import sleep
from web_crawler.utils.crawler_base import CrawlerBase


class DaumBlogCrawler(CrawlerBase):
    def __init__(self, keyword, max_page_no, driver_path, ip_bypass_flag):
        super(DaumBlogCrawler, self).__init__(keyword, max_page_no, driver_path, ip_bypass_flag)

    def __call__(self) -> None:
        blog_title, blog_contents = self._crawling()
        self._to_csv(blog_title, blog_contents)

    @property
    def get_url(self) -> str:
        main_url = f"https://search.daum.net/search?w=blog&f=section&SA=daumsec&lpp=10&nil_src=blog&q={self.keyword}"
        sub_url = f"&sort=timely&page="

        return main_url, sub_url

    def _crawling(self) -> list:
        blog_title_list = list()
        blog_content_list = list()

        for page_no in range(1, self.max_page_no + 1):
            home_url = self.main_url + self.sub_url + str(page_no)

            self._driver.get(home_url)
            self._driver.implicitly_wait(3)

            blog_url_list = self._driver.find_elements_by_partial_link_text('blog')
            blog_url_list = [blog_url.text for blog_url in blog_url_list]

            for blog_url in blog_url_list:
                self._driver.get("https://" + blog_url)
                self._driver.implicitly_wait(3)

                try:
                    blog_title = self._driver.find_element_by_xpath(
                        '//*[@id="container"]/main/div[2]/div[2]/div[1]/div/div[1]/h2')
                    blog_content = self._driver.find_element_by_xpath('//*[@id="container"]/main/div[2]/div[2]/div['
                                                                      '2]/div')
                except:
                    print(f"{page_no}번째 페이지의 {blog_url} 크롤링 실패")
                    self.error_count += 1
                    continue

                # delay_time = random.randint(0, 5)
                # sleep(delay_time)

                blog_title_list.append(blog_title.text)
                blog_content_list.append(blog_content.text)

        return blog_title_list, blog_content_list

    def _to_csv(self, title, contents):
        blog_text_df = pd.DataFrame({'blog_title': title, 'blog_content': contents})
        blog_text_df.to_csv(
            f'daum_blog_text_data{self.max_page_no * 10 - self.error_count}.csv',
            header=True,
            index=True,
            encoding='utf-8-sig'
        )
        print(f"총 {self.max_page_no * 10 - self.error_count}개의 다음 블로그 데이터 수집 완료")
