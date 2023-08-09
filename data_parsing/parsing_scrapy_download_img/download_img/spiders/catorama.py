import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from download_img.items import CastoramaItem


class CatoramaSpider(scrapy.Spider):
    name = "catorama"
    allowed_domains = ["castorama.ru"]
    start_urls = ["https://www.castorama.ru/gardening-and-outdoor/sauna/"]

    def parse(self, response: HtmlResponse):
        link_list = response.css("a.product-card__name::attr(href)").getall()
        for link in link_list:
            yield response.follow(link, callback=self.get_info)

    def get_info(self, response: HtmlResponse):
        loader = ItemLoader(item=CastoramaItem(), response=response)
        loader.add_css('tittle_of_item', 'h1.product-essential__name::text')
        loader.add_css('price', 'span.price > span > span::text')
        loader.add_css('currency', 'span.price > span > .currency::text')
        loader.add_css('country_of_manufacturing',
                       "div.product-specifications > dl.specs-table > dd:nth-of-type(3)::text")
        loader.add_css('type_of_product',
                       "div.product-specifications > dl.specs-table > dd:nth-of-type(4)::text")
        loader.add_css('article_number',
                       "div.product-specifications > dl.specs-table > dd:nth-of-type(2)::text")
        loader.add_css('photos', 'img.top-slide__img::attr(data-src)')
        loader.add_value('url', response.url)
        yield loader.load_item()