import pandas as pd
import random
from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller


class BlogCrawler:
    def __init__(self, keyword, page_no, driver_url):
        self.keyword = keyword
        self.max_page_no = page_no

        try:
            self.driver = webdriver.Chrome(f"{driver_url}")
        except:
            chromedriver_autoinstaller.install(True)
            self.driver = webdriver.Chrome(f"{driver_url}")

        self.main_url = "https://section.blog.naver.com/Search/Post.naver?pageNo="
        self.sub_url = f"&rangeType=ALL&orderBy=sim&keyword={self.keyword}"

    def __call__(self) -> None:
        blog_title, blog_contents = self._blog_crawling()
        self._crawling_data_to_csv(blog_title, blog_contents)

    def _blog_crawling(self):
        blog_title_list = list()
        blog_content_list = list()

        for page_no in range(1, self.max_page_no + 1):
            url = self.main_url + str(page_no) + self.sub_url

            self.driver.get(url)
            self.driver.implicitly_wait(3)

            delay_time = random.randint(0, 10)
            sleep(delay_time)

            try:
                for blog_no in range(1, 8):
                    blog_title = self.driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/div[{blog_no}]'
                                                                   f'/div/div[1]/div[1]/a[1]/strong/span')

                    blog_content = self.driver.find_element_by_xpath(f'//*[@id="content"]/section/div[2]/div[{blog_no}]'
                                                                     f'/div/div[1]/div[1]/a[2]')

                    blog_title_list.append(blog_title.text)
                    blog_content_list.append(blog_content.text)

            except:
                print(f"{page_no}번째 page {blog_no}번째 게시글에서 오류발생")

        return blog_title_list, blog_content_list

    def _crawling_data_to_csv(self, title, contents):
        blog_text_df = pd.DataFrame({'blog_title': title, 'blog_content': contents})
        blog_text_df.to_csv(f'blog_text_data{self.max_page_no * 7}.csv', header=True, index=True, encoding='utf-8-sig')
