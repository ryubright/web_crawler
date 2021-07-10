import pandas as pd
import random
from time import sleep
from web_crawler.utils.crawling_base import CrawlingBase


class NaverBlogCrawler(CrawlingBase):
    def __init__(self, keyword, max_page_no, driver_path):
        super(NaverBlogCrawler, self).__init__(keyword, max_page_no, driver_path)

    def __call__(self) -> None:
        blog_titles, blog_contents = self._crawling()
        self._to_csv(blog_titles, blog_contents)

    @property
    def get_url(self) -> str:
        main_url = "https://section.blog.naver.com/Search/Post.naver?pageNo="
        sub_url = f"&rangeType=ALL&orderBy=sim&keyword={self.keyword}"

        return main_url, sub_url

    def _crawling(self) -> list:
        blog_title_list = list()
        blog_content_list = list()

        for page_no in range(1, self.max_page_no + 1):
            url = self.main_url + str(page_no) + self.sub_url

            self._driver.get(url)
            self._driver.implicitly_wait(3)

            delay_time = random.randint(0, 10)
            sleep(delay_time)

            try:
                for blog_no in range(1, 8):
                    blog_title = self._driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/div[{blog_no}]'
                                                                    f'/div/div[1]/div[1]/a[1]/strong/span')

                    blog_content = self._driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/'
                                                                      f'div[{blog_no}]/div/div[1]/div[1]/a[2]')

                    blog_title_list.append(blog_title.text)
                    blog_content_list.append(blog_content.text)
            except:
                self.error_count += 1
                print(f"{page_no}번째 page {blog_no}번째 게시글에서 오류발생")

        return blog_title_list, blog_content_list

    def _to_csv(self, titles, contents):
        blog_text_df = pd.DataFrame({'blog_title': titles, 'blog_content': contents})
        blog_text_df.to_csv(
            f'naver_blog_text_data{self.max_page_no * 7 - self.error_count}.csv',
            header=True,
            index=True,
            encoding='utf-8-sig'
        )
        print(f"총 {self.max_page_no * 7 - self.error_count}개의 블로그 데이터 수집 완료")
