import scrapy
import re
from scrapy.loader.processors import MapCompose, Compose, TakeFirst


def convert_price(price):
    if price[0]:
        price = int(price[0])
    return price


def process_photo(photo):
    if photo:
        photo = 'https://www.castorama.ru' + photo
    return photo


def convert_data_str(data):
    if data[0].startswith('\n'):
        data = re.sub(r'\n', '', data[0])
    data = data.strip()
    return data


class CastoramaItem(scrapy.Item):
    tittle_of_item = scrapy.Field(input_processor=Compose(convert_data_str), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(convert_price), output_processor=TakeFirst())
    currency = scrapy.Field(output_processor=TakeFirst())
    type_of_product = scrapy.Field(input_processor=Compose(convert_data_str),output_processor=TakeFirst())
    country_of_manufacturing = scrapy.Field(input_processor=Compose(convert_data_str),output_processor=TakeFirst())
    article_number = scrapy.Field(input_processor=Compose(convert_data_str),output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(process_photo))
    url = scrapy.Field(output_processor=TakeFirst())
