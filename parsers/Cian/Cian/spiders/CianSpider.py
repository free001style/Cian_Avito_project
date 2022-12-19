import scrapy
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import urljoin
import re
import json
from Cian.items import CianItem

API = 'c87970fe805bdd1483d16628868a0ba1'
pages = [i for i in range(1, 15)]


def get_url(url):
    payload = {'api_key': API, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class CianspiderSpider(scrapy.Spider):
    name = 'CianSpider'

    def start_requests(self):
        for page in pages:
            url = 'https://novosibirsk.cian.ru/cat.php?' + urlencode(
                {'deal_type': 'sale', 'engine_version': '2', 'object_type%5B0%5D': '1', 'offer_type': 'flat',
                 'region': '4897',
                 'p': str(page)})
            yield scrapy.Request(url=get_url(url), callback=self.parse_keyword_response)

    def parse_keyword_response(self, response):
        flats = set()
        for res in response.xpath(
                '//article[contains(@data-name,"CardComponent")]//div[contains(@data-name,"LinkArea")]/a/@href').extract():
            flats.add(res)

        for flat in flats:
            yield scrapy.Request(url=get_url(flat), callback=self.parse_product_page)

    def parse_product_page(self, response):
        item = CianItem()
        name = response.xpath('//h1[contains(@class, "a10a3f92e9--title--UEAG3")]/text()').extract()
        price = response.xpath('//span[contains(@itemprop,"price")]/text()').extract()
        address = response.xpath('//address[contains(@class,"a10a3f92e9--address--F06X3")]/a/text()').extract()
        available_metro_station = response.xpath(
            '//li[contains(@class,"a10a3f92e9--underground--wH2F4")]/a/text()').extract()
        total_information = response.xpath(
            '//div[contains(@data-testid,"object-summary-description-info")]/div/text()').extract()
        description = response.xpath('//p[contains(@class,"a10a3f92e9--description-text--YNzWU")]/text()').extract()
        photos = response.xpath('//li[contains(@class, "a10a3f92e9--container--Havpv")]/img/@src').extract()

        item['name'] = ''.join(name).strip()
        item['price'] = ''.join(price).strip()
        item['address'] = ''.join(address).strip()
        item['available_metro_station'] = ''.join(available_metro_station).strip()
        item['description'] = ''.join(description).strip()
        item['total_information'] = ''.join(total_information).strip()
        item['photos'] = ''.join(photos).strip()
        item['coords'] = ""
        yield item
