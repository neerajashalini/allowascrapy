# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AllowdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
import scrapy



class alldemoItem(scrapy.Item):
     
event_name = scrapy.field()
event_date_time = scrapy.field()
address = scrapy.field()
images = scrapy.field()
organizer = scrapy.field()
description =  scrapy.field() 
follow = scrapy.field() 