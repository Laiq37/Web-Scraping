# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotetutorialPipeline:
    def process_item(self, item, spider):
        
        print('Pipeline_tags: ',end="")
        for tag in item['Tags']:
            print(f'{tag}',end=", ")
        print(f"\nPipeline_Quote : {item['Quotes']}\nPipeline_Author: {item['Author']}")
        
        return item
