import scrapy

class articles(scrapy.Spider):
    name = "articles"
    start_urls = ['https://www.bbc.com/sport/football/champions-league']

    def parse(self, response):
        # Extract article links
        article_links = response.css('li > div > div > div > div > div > a::attr(href)').getall()

        for link in article_links:
            yield response.follow(link, callback=self.parse_article)

    def parse_article(self, response):
        title = response.css('h1::text').get()
        text = response.css('article > div > p > span::text').getall()

        if(text != []):
            yield {
                'title': title,
                'text': text
            }   