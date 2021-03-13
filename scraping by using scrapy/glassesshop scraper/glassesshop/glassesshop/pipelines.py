# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class GlassesshopPipeline:
    def process_item(self, item, spider):
        return item
    
class GlassesshopImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [scrapy.Request(x, meta={'image_name': item["Name"],"image_no":item['no']}) 
                for x in item.get('image_urls', [])]

    def file_path(self, request, response=None, info=None):
        return f'{str(request.meta["image_no"])}. {request.meta["image_name"]}.jpg'