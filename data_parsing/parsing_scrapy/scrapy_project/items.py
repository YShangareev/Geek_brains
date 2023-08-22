import re
import scrapy
from scrapy.loader.processors import MapCompose, Compose, TakeFirst


def convert_data(data):
    if data:
        substring = re.compile(r'\xa0')
        data = re.sub(substring, '', data)
    else:
        data = None
    return data

def convert_currency(data):
    if data:
        substring = re.compile(r'\xa0')
        data = re.sub(substring, '', data[0])
    else:
        data = None
    return data


class AvitoItem(scrapy.Item):
    tittle_of_item = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(convert_data), output_processor=TakeFirst())
    currency = scrapy.Field(input_processor=Compose(convert_currency), output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
