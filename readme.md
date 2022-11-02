# Scrapy Tutorials

1. Create scrapy projects
    ```
    scrapy startproject tutorial
    ```

2. Move to your project directory
    ```
    cd tutorial
    ```

3. Write spider class inside tutorial/spiders/
   ```
   # file: header_one_spider.py

   import scrapy

   class HeaderOneScrapy(scrapy.Spider):
        name = "header_one"
        
        def start_request(self):
            urls = [
            "https://docs.scrapy.org/en/latest/intro/tutorial.html"
            ]

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
        
        def parse(self):
            yield {
                "h1": response.css("h1::text").getall()
            }
   ```

4. Start scrapy crawler from your project directory
   ```
   scrapy crawl header_one
   ```
   header_one is your spider name, it is defined in the above class.


5. Store the scraped data
   ```
   scrapy crawl header_one -O header_one.json
   ```

