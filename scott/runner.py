# from scrapy.utils.project import get_project_settings
# from scrapy.crawler import CrawlerProcess

# setting = get_project_settings()
# process = CrawlerProcess(setting)

# for spider_name in process.spiders.list():
#     print ("Running spider %s" % (spider_name))
# #     process.crawl(spider_name,query="dvh") #query dvh is custom argument used in your scrapy

# # process.start()
from scrapy import spiderloader    
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

settings = get_project_settings()
process = CrawlerProcess(settings)
spider_loader = spiderloader.SpiderLoader.from_settings(settings)

for spider_name in spider_loader.list():
    print("Running spider %s" % (spider_name))
    process.crawl(spider_name)
process.start()