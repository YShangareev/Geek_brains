import scrapy
import hashlib
from scrapy.utils.python import to_bytes
from scrapy.pipelines.images import ImagesPipeline

class DownloadImgPipeline:
    def process_item(self, item, spider):
        print()
        return item

class CastoramaPhoto(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for photo in item['photos']:
                try:
                    yield scrapy.Request(photo)
                except Exception as e:
                    print(f'Ошибка {e}')

    def file_path(self, request, response=None, info=None, *, item=None):
        if item['article_number']:
            try:
                folder = item['article_number']
                image_guid = image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
                return f"{folder}/{image_guid}.jpg"
            except Exception as e:
                print(f'Ошибка {e}')