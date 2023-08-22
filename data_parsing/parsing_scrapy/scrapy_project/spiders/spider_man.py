import scrapy
from scrapy_splash import SplashRequest
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from scrapy_project.items import AvitoItem

class SpiderManSpider(scrapy.Spider):
    name = "spider_man"
    allowed_domains = ["avito.ru"]
    start_urls = [
        'https://www.avito.ru/ufa/igry_pristavki_i_programmy/igrovye_pristavki-ASgBAgICAUSSAsoJ?cd=1&q=playstation+5']

    def start_requests(self):

        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse)

    def parse(self, response: HtmlResponse):
        elements = response.xpath("//h3[@itemprop]/../@href").getall()
        for element in elements:
            link = 'https://www.avito.ru' + element
            yield SplashRequest(url=link, callback=self.get_info, args={'wait': 10})

    # def get_image(self, response: HtmlResponse):
        # js_script = """
        #             var elements = document.querySelectorAll("li.images-preview-previewImageWrapper-RfThd");
        #             var results = [];
        #             for (var i = 0; i < elements.length; i++) {
        #                 var element = elements[i];
        #                 element.click();
        #                 await new Promise(resolve => setTimeout(resolve, 500));
        #                 var img = document.querySelector("div.image-frame-wrapper-_NvbY > img");
        #                 if (img) {
        #                     results.push(img.getAttribute("src"));
        #                 }}
        # """

        # yield SplashRequest(url=response.url, callback=self.get_info, args={'lua_source': js_script})

    def get_info(self, response: HtmlResponse):
        loader = ItemLoader(item=AvitoItem(), response=response)
        loader.add_css('tittle_of_item', 'h1 > span::text')
        loader.add_css('price', "span.style-price-value-main-TIg6u:nth-of-type(1) > span[itemprop='price']::text")
        loader.add_css('currency', "span[itemprop='priceCurrency']::text")
        loader.add_css('description', "div[itemprop='description']::text")
        loader.add_css('photos', 'div.image-frame-wrapper-_NvbY > img::attr(src)')
        loader.add_css('photos', 'li > img::attr(src)')
        loader.add_value('url', response.url)
        yield loader.load_item()
