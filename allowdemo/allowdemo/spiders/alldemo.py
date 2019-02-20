import scrapy
import re

class alldemo(scrapy.Spider):
	name = "all_spider"
	   start_urls = ["http://allevents.in/new%20delhi/all"]
	     npages = 1
	for i in range(1,15):
		 start_urls.append("http://allevents.in/new%20delhi/all?page="+str(i)+"")
		def parse(self,response):
			for href in response.xpath("//div[contains(@class,'pagination elist-pager')]/li//@href"):
			url = "http://allevents.in/new%20delhi/all"+href.extract()
				yield scrapy.request(url,callback=self.parse_dir_contents)
		def parse_dir_contents(self,response):
			item = alldemoItem()
		     item['event_name'] = response.xpath("//div[contains(@class,'pd-lr-10 span9')]//text()").extract()
		item['event_date'] = response.xpath("//ul[contains(@class ,'meta-list')]/span[contains(@class,'label label-normal hidden-phone')]/descendant::text()").extract()
		    item['event_time'] =response.xpath("//ul[contains(@class ,'meta-list')]/span[contains(@class,'label label-normal hidden-phone')]/descendant::text()").extract()
			 item['event_date_time'] = "".join(event__date)" ".join(event_time)""
			 item['address'] = response.xpath("//span[contains(@class,'full venue')]/text()").extract()
			item['images'] = response.xpath("//div[contains(@class,'span3 event-thumb-parent')]/img[contains(@class,'event-banner-img')]/text()").extract()
			name= response.xpath ("//div[contains(@class,'name')]/descendant::text()").extract()
			imag= response.xpath ("//div[contains(@class,'thumb')]/a[contains(@href)]/img)]/descendant::text()").extract()
			view= response.xpath ("//div[contains(@class,'bottom')]/a/[contains(@href0]/descendant::text()").extract()
			item['organizer']=  "".join(name)" ".join(imag)" ".join(view)""
			item['description'] = response.xpath("//div[contains(@class,'event-description-html')]/text()").extract()
		    item['follow'] = response.xpath("//a[contains(@class ,'btn btn-follow follow-action tltp track'/text()").extract()
		    yield item