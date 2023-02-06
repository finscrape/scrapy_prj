import scrapy
import json
from scrapy_selenium import SeleniumRequest
import pandas as pd

df = pd.read_excel('codes.xlsx')
df1 = pd.read_excel('listss.xlsx')

cd = list(df['postcode'])
cd1 = list(df1['links'])
class HomesSpider(scrapy.Spider):
    name = 'homes'
    # allowed_domains = ['a.com']
    # start_urls = ['http://a.com/']
    def __init__(self):
        self.postcd = None

    def start_requests(self):
        for i in cd[0:1000]:
            self.postcd = i
            x = i.split()
            pp = '%20'.join(x)
            p = pp.lower()


    
            yield SeleniumRequest(url=f'https://scotlis.ros.gov.uk/public/bff/land-register/addresses/?postcode={p}',wait_time=2)
        
    def parse(self, response):
        print(response.body)
        xx = response.xpath("//body/pre/descendant::text()").getall()
        xxx = "".join(xx)
    
        html = json.loads(xxx)
        xv = html.get('_embedded')
        if xv:
            x = xv.get('addresses')
        
            for i in x:
                each = i.get('titles')
                e = each[0]
                ai = e.get('addressIndex')
                tn = e.get('titleNumber')
                print(f'{ai}:{tn}')
                
                urll = f'https://scotlis.ros.gov.uk/public/bff/land-register/titles/{tn}/{ai}'
            
                yield SeleniumRequest(url=urll,callback=self.end,meta={"i":tn,'ii':ai})

    def end(self,response):
        tn = response.meta['i']
        ai = response.meta['ii']
        
        xx = response.xpath("//body/pre/descendant::text()").getall()
        xxx = "".join(xx)
        html = json.loads(xxx)
        addr = html.get('prettyAddress')
        pr = html.get('lastPurchasePrice')
        prd = html.get('lastPurchaseDate')
        rs = html.get('registrationStatus')
        it = html.get('interest').get('type')
        pt = html.get('classification')

        urll = f'https://scotlis.ros.gov.uk/public/bff/land-register/prices/{tn}'
            
        yield SeleniumRequest(url=urll,callback=self.last,meta={"i":tn,'ii':ai,'ad':addr,'pr':pr,'prd':prd,'rs':rs,'it':it,'pt':pt})

    def last(self,response):  
        tn = response.meta['i']
        ai = response.meta['ii']
        addr = response.meta['ad']
        pr = response.meta['pr']
        prd = response.meta['prd']
        it = response.meta['it']
        rs = response.meta['rs']
        pt = response.meta['pt']

        xx = response.xpath("//body/pre/descendant::text()").getall()
        xxx = "".join(xx)
        html = json.loads(xxx)

        li = []
        h = html.get('_embedded').get('housePrices')
        for i in h:
            a = i.get('consideration')
            b = i.get('entryDate')

            c = f'{b}:{a}'
            li.append(c)
         
        yield {
            'Title_Number':tn,
            'Address':addr,
            'Purchase_price':pr,
            'Purchase_date':prd,
            'Land register':rs,
            'Interest':it,
            'Property_type':pt,
            'Postcode':self.postcd,
            'historical_prices':li
        }

        
        # for i in x:
        #     li = i.get('titles')
        #     xx = li[0]
        #     print(xx)
