import scrapy
from scrapy.http.response.html import HtmlResponse


class HeaderOneSpider(scrapy.Spider):
    name = "header_one"
    
    def start_requests(self):
        urls = [
            "https://docs.scrapy.org/en/latest/intro/tutorial.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        yield {
            "h1": response.css("h1::text").getall()
        }

        