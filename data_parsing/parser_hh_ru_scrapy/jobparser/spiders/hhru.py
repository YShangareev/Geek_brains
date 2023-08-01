import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = [
        "https://hh.ru/search/vacancy?search_field=name&area=1&search_field=company_name&search_field=description&enable_snippets=false&text=data+scientist&items_on_page=20",
        ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        link_list = response.xpath("//a[@class='serp-item__title']/@href").getall()
        for link in link_list:
            yield response.follow(link, callback=self.get_info)

    def get_info(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='bloko-header-section-1']/text()").get()
        if name is None:
            name = response.xpath("//h1[@class='bloko-header-1']/text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']/span[contains(@class,'bloko-header-section-2_lite')]//text()").getall()
        experience = response.xpath("//span[@data-qa='vacancy-experience']/text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, experience=experience, url=url)
