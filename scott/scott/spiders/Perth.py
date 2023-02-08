import scrapy
import scrapy
import scrapy
import scrapy
from urllib.parse import urlparse
from pymongo import MongoClient
import certifi
ca = certifi.where()
import pymongo
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


#connecting to mongo
URI = 'mongodb+srv://Bola:Gbolyfranco21#@cluster0.ovorzhw.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(URI, tlsCAFile=ca)

db = client.get_database('scotland')
planning = db.Perth_Council
db.p_applications.create_index([('Check', pymongo.ASCENDING)], unique=True)
#end


class PerthSpider(scrapy.Spider):
    name = 'Perth'
    # allowed_domains = ['a.com']
    # start_urls = ['http://a.com/']

    def __init__(self):
        self.key = 0
        self.num = 0

    def start_requests(self):
        #moray,perth,west dunbarnton
        ii = ['https://publicaccess.aberdeencity.gov.uk/online-applications/search.do?action=property&type=atoz']
        
        
        for i in ii:
        
        
        
        
            yield scrapy.Request(url=i,meta={'f':i})
    def parse(self, response):
        fir = response.meta['f']
        head = urlparse(fir).netloc
#         h = f'https://{head}'
        
        
#         first = f'{fir}&letter=A'
#         l = response.xpath("//li/a[contains(@title,'Streets beginning with the letter')]/@href").getall()
#         l.append(first)
#         for i in l:
#             if 'http' not in i:
#                 i = f'{h}{i}'
            
#                 yield scrapy.Request(url=i,dont_filter=True,callback=self.each,meta={'h':h})
#             else:
#                 yield scrapy.Request(url=i,dont_filter=True,callback=self.each,meta={'h':h})


#     def each(self,response):
#         h = response.meta['h']
#         next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
#         l = response.xpath("//ul[@id='streetlist']/li/a/@href").getall()
#         for i in l:
#             if 'http' not in i:
#                 i = f'{h}{i}'
#                 yield scrapy.Request(url=i,meta={'h':h},callback=self.street)
#             else:
#                 yield scrapy.Request(url=i,meta={'h':h},callback=self.street)
            

#         if next:

#             ab_next = f'{h}{next}'
#             yield scrapy.Request(url=ab_next,callback=self.each,meta={'h':h})
#             print('mooooooooooooooooooooooving one battch')

        

#     def street(self,response):
#         h = response.meta['h']
#         urp = response.xpath("//th[text()='UPRN:']/following-sibling::td/text()").get()
#         next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
#         link = response.xpath("//ul[@id='searchresults']/li/a/@href").getall()
#         if link:
#             for i in link:
#                 ii = f'{h}{i}'
#                 yield scrapy.Request(url=ii,callback=self.pty,meta={'h':h})
#         elif urp is not None:
#             current = response.url
#             yield scrapy.Request(url=current,callback=self.pty,meta={'h':h},dont_filter=True)

        
        
        
#         if next:
#             ab_next = f'{h}{next}'
#             yield scrapy.Request(url=ab_next,callback=self.street,meta={'h':h})
            
#     def pty(self,response):
#         h = response.meta['h']
#         urpn = response.xpath("//th[text()='UPRN:']/following-sibling::td/text()").get()
#         link = response.xpath("//li/a[contains(span/text(),'Property History')]/@href").get()
#         if link:
#             a_link = f'{h}{link}'
#             yield scrapy.Request(url=a_link,meta={'h':h,'u':urpn},callback=self.info)

#     def info(self,response):
#         h = response.meta['h']
#         u = response.meta['u']
        
#         link = response.xpath("//div[@id='relatedItems']/div")
#         for i in link[0:1]:
#             title = i.xpath('.//@id').get()
#             li = i.xpath(".//ul/li/a/@href").getall()
#             if li:
#                 for i in li:
#                     if i:
#                         a_li = f'{h}{i}'
#                         yield scrapy.Request(url=a_li,meta={'h':h,'t':title,'u':u},callback=self.last)

#     def last(self,response):
#         dic = {}
#         urpn = response.meta['u']
#         title = response.meta['t']
#         h = response.meta['h']
#         curl = response.url

#         #dic['urpn'] = urpn
#         #dic['title'] = title
        
#         attr = response.xpath("//table[@id='simpleDetailsTable']/tr")
#         if attr:
#             reference = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[1]/td/descendant::text())").get()    
#             a_reference = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[2]/td/descendant::text())").get()    
#             a_received = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[3]/td/descendant::text())").get()    
#             a_validated = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[4]/td/descendant::text())").get()    
#             addr = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[5]/td/descendant::text())").get()    
#             propose = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[6]/td/descendant::text())").get()    
#             stat = response.xpath("//table[@id='simpleDetailsTable']/tr[7]/td/descendant::text()").getall()
#             status = ''.join(stat)    
#             st = status.strip()
#             decision = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[8]/td/descendant::text())").get()    
#             did = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[9]/td/descendant::text())").get()    
#             a_status = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[10]/td/descendant::text())").get()    
#             a_decision = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[11]/td/descendant::text())").get()    
#             doc = response.xpath("//li[contains(a/span/text(),'Documents')]/a/@href").get()
#             docu = f'{h}{doc}'

#             rela = response.xpath("//li[contains(a/span/text(),'Related')]/a/@href").get()
#             related = f'{h}{rela}'

#             cont = response.xpath("//li[contains(a/span/text(),'Contacts')]/a/@href").get()
#             contacts = f'{h}{cont}'
#             self.num += 1
#             self.key = f'{urpn}-{self.num}'

#             result = {
#                 'Title':title,
#                 'URPN':urpn,
#                 'Reference':reference,
#                 'Alternative_reference':a_reference,
#                 'Application_received':a_received,
#                 'Application_validated':a_validated,

#                 'Address':addr,
#                 'Proposal':propose,
#                 'Status':st,
#                 'Decision':decision,
#                 'Decision_issued_date':did,
#                 'Appeal_status':a_status,
#                 'Appeal_decision':a_decision,
#                 'Source_link':curl,
#                 'Document_link':docu,
#                 'Related_cases':related,
#                 'Contacts':contacts,
#                 'Check':self.key
                
#             }
#             planning.insert_one(result)
#             yield result

