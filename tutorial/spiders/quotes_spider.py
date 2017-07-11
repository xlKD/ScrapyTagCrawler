import scrapy

from tutorial.items import TutorialItem

class TagsSpider(scrapy.Spider):
    name = "tags"
    domain = "http://www2.hm.com"
    start_urls = [
        'http://www2.hm.com/ja_jp/men/shop-by-product/view-all.html?product-type=men_all&sort=stock&offset=0&page-size=30',
    ]

    def parse(self, response):
        links = response.css('a.product-item-link::attr(href)').extract()
        for link in links:
            yield scrapy.Request(self.domain + link, callback=self.parseItem)

    def parseItem(self, response):
        # yield {
        #     'title' : response.css('h1.product-item-headline::text').extract_first(),
        #     'images' : response.css('img.product-detail-thumbnail-image::attr(src)').extract()
        # }
        # grab the URL of the cover image
        img_urls = response.css('img.product-detail-thumbnail-image::attr(src)').extract()
        for img_url in img_urls:
            img_url = img_url.replace('/thumb', '/main')
            yield TutorialItem(image_urls=['http:' + img_url])
