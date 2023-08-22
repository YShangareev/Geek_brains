import scrapy
import hashlib
import pymongo
from scrapy.utils.python import to_bytes
from scrapy.pipelines.images import ImagesPipeline


class AvitoPhotoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for photo in item['photos']:
                try:
                    yield scrapy.Request(photo)
                except Exception as e:
                    print(f'Ошибка {e}')

    def file_path(self, request, response=None, info=None, *, item=None):
        if item['tittle_of_item']:
            try:
                folder = item['tittle_of_item']
                image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
                return f"{folder}/{image_guid}.jpg"
            except Exception as e:
                print(f'Ошибка {e}')


class AddMongoPipeline:
    def __init__(self, mongo_client, mongo_db):
        self.mongo_client = mongo_client
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_client=crawler.settings.get('MONGO_CLIENT'),
                   mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_client)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection_name = spider.settings.get('MONGO_COLLECTION')
        collection = self.db[collection_name]
        collection.update_one({'url': item['url']}, {'$set': dict(item)}, upsert=True)
        return item
