import requests
from pip._vendor.msgpack.fallback import xrange

import csv

from QYspider.spider import spider
from QYspider.parser import parser


class lianjia_spider(spider):
    def __init__(self, url="") -> object:
        super().__init__()
        self.url = 'https://lz.lianjia.com/ershoufang/rs{}/'
        print(self.type)

    def execute(self, ps: parser):
        super().execute(ps)

        # print(title)
        # return houseInfo,title,positionInfo,totalPrice,unitPrice,followInfo,tag
