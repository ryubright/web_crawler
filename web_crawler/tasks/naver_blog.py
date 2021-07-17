import pandas as pd
import random
from time import sleep
from web_crawler.utils.crawler_base import CrawlerBase


class NaverBlogCrawler(CrawlerBase):
    def __init__(self, keyword, max_page_no, driver_path, ip_bypass_flag):
        super(NaverBlogCrawler, self).__init__(keyword, max_page_no, driver_path, ip_bypass_flag)

    def __call__(self) -> None:
        blog_titles, blog_contents, blog_dates = self._crawling()
        self._to_csv(blog_titles, blog_contents, blog_dates, self.count)

    @property
    def get_url(self) -> str:
        main_url = "https://section.blog.naver.com/Search/Post.naver?pageNo="
        sub_url = f"&rangeType=ALL&orderBy=recentdate&keyword={self.keyword}"

        return main_url, sub_url

    def _crawling(self) -> list:
        blog_title_list = []
        blog_content_list = []
        blog_date_list = []

        for page_no in range(1, self.max_page_no + 1):
            url = self.main_url + str(page_no) + self.sub_url

            self._driver.get(url)
            self._driver.implicitly_wait(3)

            # delay_time = random.randint(0, 10)
            # sleep(delay_time)

            try:
                for blog_no in range(1, 8):
                    blog_title = self._driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/div[{blog_no}]'
                                                                    f'/div/div[1]/div[1]/a[1]/strong/span')

                    blog_content = self._driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/'
                                                                      f'div[{blog_no}]/div/div[1]/div[1]/a[2]')

                    blog_date = self._driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/div[{blog_no}]/'
                                                                   f'div/div[1]/div[2]/span[2]')

                    blog_title_list.append(blog_title.text)
                    blog_content_list.append(blog_content.text)
                    blog_date_list.append(blog_date.text)

                    self.count += 1

                    if self.count % 5000 == 0:
                        self._to_csv(blog_title_list, blog_content_list, blog_date_list, self.count)
                        blog_title_list = []
                        blog_content_list = []
                        blog_date_list = []

            except:
                self.error_count += 1
                print(f"{page_no}번째 page {blog_no}번째 게시글에서 오류발생")

        return blog_title_list, blog_content_list, blog_date_list

    def _to_csv(self, titles, contents, dates, counts):
        blog_text_df = pd.DataFrame({'blog_title': titles, 'blog_content': contents, 'blog_date':dates})

        if counts < 5000:
            file_path = f"naver_blog_text_data{counts}.csv"
        else:
            file_path = f"naver_blog_text_data{5000 - counts}_{counts}.csv"

        blog_text_df.to_csv(
            file_path,
            header=True,
            index=True,
            encoding='utf-8-sig'
        )

        print(f"{file_path} 생성")
