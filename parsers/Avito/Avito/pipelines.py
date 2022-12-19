# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AvitoPipeline:
    def open_spider(self, spider):
        self.file = open("Avito_flats_spb.json", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # if item['mortgage'] == 'что-то':  # TODO add mortage
        line = json.dumps(ItemAdapter(item).asdict(), indent=8, ensure_ascii=False) + ',' + '\n'
        self.file.write(line)
        return item
