# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SinaNewsItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pub_date = scrapy.Field()
    source = scrapy.Field()
    keywords = scrapy.Field()
