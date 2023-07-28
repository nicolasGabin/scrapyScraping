import scrapy

class topScorers(scrapy.Spider):
    name = "fixtures"

    def start_requests(self):
        urls = [
                "https://www.bbc.com/sport/football/champions-league/scores-fixtures"
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {

        }