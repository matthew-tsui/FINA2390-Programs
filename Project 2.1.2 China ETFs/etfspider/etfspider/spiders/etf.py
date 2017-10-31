import scrapy
import requests
from lxml import html


USERNAME = "14714407056"
PASSWORD = "hkufina123"
LOGIN_URL = "http://dc.simuwang.com/"
URL = "https://dc.simuwang.com/"

class EtfSpider(scrapy.Spider):
    name = 'etf'
    allowed_domains = ['simuwang.com']
    start_urls = ('http://dc.simuwang.com/',)

    def parse(self, response):
        filename = response.url.split('/')[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        rows = response.xpath('//*[@id="tab-1-1"]/table/tbody/tr')
        for row in rows:
            col = row.select('td')
            for value in col:
                print value.select('text()').extract()
                
            #etf = EtfspiderItem()

            #etf['ranking'] = items_tr.select('td/text()').extract()