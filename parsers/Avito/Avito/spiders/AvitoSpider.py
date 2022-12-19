import scrapy
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import urljoin
import re
import json
from Avito.items import AvitoItem

API = ''  # вставляй свой
pages = [i for i in range(1, 9)]


def get_url(url):
    payload = {'api_key': API, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class AvitospiderSpider(scrapy.Spider):
    name = 'AvitoSpider'

    def start_requests(self):
        for page in pages:
            url = 'https://www.avito.ru/sankt-peterburg/kvartiry/prodam/vtorichka?' + urlencode({'p': str(page)})
            yield scrapy.Request(url=get_url(url), callback=self.parse_keyword_response)

    def parse_keyword_response(self, response):
        flats = set()
        for res in response.xpath(
                '//div[contains(@class,"iva-item-titleStep-pdebR")]/a/@href').extract():
            flats.add('https://www.avito.ru' + res)

        for flat in flats:
            yield scrapy.Request(url=get_url(flat), callback=self.parse_product_page)

    def parse_product_page(self, response):
        item = AvitoItem()
        name = response.xpath('//span[contains(@class, "title-info-title-text")]/text()').extract()
        price = response.xpath(
            '//span[contains(@class, "js-item-price style-item-price-text-_w822 text-text-LurtD text-size-xxl-UPhmI")]/text()').extract()
        address = response.xpath('//span[contains(@class,"style-item-address__string-wt61A")]/text()').extract()
        available_metro_station = response.xpath(
            '//span[contains(@class,"style-item-address-georeferences-item-TZsrp")]/span/text()').extract()
        description = response.xpath('//div[contains(@itemprop,"description")]/p/text()').extract()
        total_information = response.xpath('//li[contains(@class, "params-paramsList__item-appQw")]//text()').extract()
        about_home = response.xpath('//li[contains(@class, "style-item-params-list-item-aXXql")]//text()').extract()
        photos = response.xpath(
            '//div[contains(@class, "image-frame-wrapper-_NvbY")]/img/@src').extract()

        item['name'] = ''.join(name).strip()
        item['price'] = ''.join(price).strip()
        item['address'] = ''.join(address).strip()
        item['available_metro_station'] = ''.join(available_metro_station).strip()
        item['description'] = ''.join(description).strip()
        item['total_information'] = ''.join(total_information).strip()[231:]
        item['about_home'] = ''.join(about_home).strip()
        item['photos'] = ''.join(photos).strip()
        item['coords'] = ""
        yield item
