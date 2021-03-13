# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class AmazonbotPipeline:
    def process_item(self, item, spider):
        csv_columns = ['name','rating','review','price','link']
        csv_file = "amazon_result.csv"
        try:
            try:
                with open(csv_file, 'x') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    writer.writerow(item)
            except FileExistsError:
                with open(csv_file, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writerow(item)
        except IOError:
            print("I/O error")
        return item
