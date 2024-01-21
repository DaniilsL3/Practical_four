import scrapy


class UniversityRankingSpider(scrapy.Spider):
    name = 'rankings'
    start_urls = ['https://www.shanghairanking.com/rankings/arwu/2023']

    def parse(self, response):
        rank_index = 0
        name_index = 1  # This index might need adjustment
        score_index = 4

        for row in response.css('#content-box > div.rk-table-box > table > tbody > tr'):
            columns = row.css('td')
            if len(columns) > max(rank_index, score_index):  # Assuming name is within these columns
                yield {
                    'rank': columns[rank_index].css('::text').get().strip(),
                    'name': row.css('td.align-left > div > div.tooltip > div > a > span::text').get().strip(),
                    'score': columns[score_index].css('::text').get().strip()
                }

        # Find the link to the next page using the provided selector
        next_page = response.css('#content-box > ul > li.ant-pagination-next > a::attr(href)').get()
        print(f"Next page URL: {next_page}")  # Debugging line

        # If a next page is found, follow it
        if next_page is not None:
            yield response.follow(next_page, self.parse)