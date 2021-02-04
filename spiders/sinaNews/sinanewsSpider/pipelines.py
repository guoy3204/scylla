# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class SinanewsspiderPipeline:
    collection_name = 'sina_news'

    def __init__(self, mongo_url, mongo_database):
        self.mongo_url = mongo_url
        self.mongo_database = mongo_database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('MONGO_URL'),
            crawler.settings.get('MONGO_DATABASE'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.database = self.client.get_database(self.mongo_database)
        self.collection = self.database.get_collection(self.collection_name)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.find_and_modify({ "_id": item['_id'] } ,dict(item), upsert=True)
        return item