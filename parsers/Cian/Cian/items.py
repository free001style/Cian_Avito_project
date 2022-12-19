# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CianItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    available_metro_station = scrapy.Field()
    description = scrapy.Field()
    total_information = scrapy.Field()
    about_home = scrapy.Field()
    photos = scrapy.Field()
    coords = scrapy.Field()
