from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from scrapy import Spider
from scrapy.selector import Selector
import time


# A Selenium based Scrapy spider with pagination.
class UniversityRankingSpider(Spider):
    name = 'rankings_selenium'

    def __init__(self, year=None, *args, **kwargs):
        super(UniversityRankingSpider, self).__init__(*args, **kwargs)
        self.year = year
        self.allowed_domains = ['shanghairanking.com']
        self.start_urls = [f'https://www.shanghairanking.com/rankings/arwu/{year}']  # URL for a specific year
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)

        while True:
            sel = Selector(text=self.driver.page_source)
            universities = sel.css('#content-box > div.rk-table-box > table > tbody > tr')

            for university in universities:
                # Extracting rank, name, and score
                rank = university.css('td:nth-child(1) > div::text').get()
                name = university.css('td.align-left div.tooltip a span::text').get()
                score = university.css('td:nth-last-child(2)::text').get()

                # Data validation
                rank = rank.strip() if rank else "Rank not found"
                name = name.strip() if name else "Name not found"
                score = score.strip() if score else "Score not found"

                yield {
                    'rank': rank,
                    'name': name,
                    'score': score
                }

            # Pagination handling
            try:
                next_page = self.driver.find_element(By.CSS_SELECTOR, '#content-box > ul > li.ant-pagination-next')
                if "disabled" in next_page.get_attribute("class"):
                    break
                next_page.click()
                time.sleep(0.15)  # Adjust sleep time as needed
            except NoSuchElementException:
                break

    def closed(self, reason):
        self.driver.close()
