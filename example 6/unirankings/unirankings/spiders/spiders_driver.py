from multiprocessing import Process, freeze_support
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from rankings_selenium import UniversityRankingSpider


# Defines a single process for one year
def run_spider(year):
    process = CrawlerProcess({
        'FEED_FORMAT': 'json',
        'FEED_URI': f'output_{year}.json'
    })
    process.crawl(UniversityRankingSpider, year=year)
    process.start()

# Use multiprocessing to crawl the rankings for 5 years in parallel
def run_spiders_for_years(years):
    processes = []
    for year in years:
        p = Process(target=run_spider, args=(year,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

# The driver to execute a Selenium based Scrapy spider for a year. Executes 5 spiders, each assigned to one process.
# Allows for concurrent scraping.
# It's a workaround for Scrapy's inbuilt concurrency ability, which is not available when using Selenium.


if __name__ == '__main__':
    freeze_support()
    years_to_scrape = ['2023', '2022', '2021', '2020', '2019']
    run_spiders_for_years(years_to_scrape)
