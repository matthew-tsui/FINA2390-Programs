# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EtfspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    fund_short_name = scrapy.Field() 
    fund_company = scrapy.Field() 
    investment_strategy = scrapy.Field()
    lastest_NAV = scrapy.Field()
    cumulative_return = scrapy.Field()
    recent_month_return = scrapy.Field()
    annalized_return = scrapy.Field()
    sharpe_ratio = scrapy.Field()
    year_rating = scrapy.Field()
    pass
