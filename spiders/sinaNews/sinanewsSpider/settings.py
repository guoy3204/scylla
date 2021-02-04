# Scrapy settings for sinanewsSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sinanewsSpider'

SPIDER_MODULES = ['sinanewsSpider.spiders']
NEWSPIDER_MODULE = 'sinanewsSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sinanewsSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
 
ITEM_PIPELINES = {
   'sinanewsSpider.pipelines.SinanewsspiderPipeline': 300,
}
 
MONGO_URL = 'mongodb://admin:Bi24ToROPrviPIuS@db.zk2x.com:27117,db.zk2x.com:27118,db.zk2x.com:27119/cms?replicaSet=threadDB&authSource=admin' 
MONGO_DATABASE = 'spider'