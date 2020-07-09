"""
爬虫Spider
"""
import csv

import requests
from lxml import etree
import time

from pip._vendor.msgpack.fallback import xrange

from QYspider.parser import parser


class spider:
    def __init__(self):
        self.iterators = {}
        self.elements = {}
        self.type = "Spider"
        self.container = dict()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def execute(self, ps: parser):
        for i in xrange(1, 21):
            url_str: str = self.url.format(i)  # 构造请求url
            rsp = requests.get(url_str, headers=self.headers)
            self.container = ps.parse_content_rsp(rsp)
            self.data_filter(i)

    def data_filter(self, page_num):

        for k in self.container:
            print(k)
            self.iterators[k] = self.iterator(k, self.container[k])

        self.save_data(page_num)

    def iterator(self, k, content):
        self.elements[k] = []
        for i in xrange(len(content)):
            yield self.elements[k][i]


    def save_data(self, page_num):
        i = 1
        k = int(str(page_num / 5).split(".")[0])
        with open("../data/lanzhou" + str(k) + ".csv", "a", newline="", encoding="utf-8-sig") as f:
            fieldnames = ['houseInfo', 'title', 'positionInfo', 'totalPrice/万元', 'unitPrice', 'followInfo', 'tag']
            writer = csv.DictWriter(f, fieldnames=fieldnames)  # 写入表头
            writer.writeheader()
            while True:
                list_2 = []
                for name in fieldnames:
                    print(self.elements)
                    list_2.append(next(self.iterators[name]))
                # data_houseInfo = next(get_houseInfo)
                # data_title = next(get_title)
                # data_positionInfo = next(get_positionInfo)
                # data_totalPrice = next(get_totalPrice)
                # data_unitPrice = next(get_unitPrice)
                # data_followInfo = next(get_followInfo)
                # data_tag = next(get_tag)
                # list_2 = [data_houseInfo, data_title, data_positionInfo, data_totalPrice, data_unitPrice,
                #           data_followInfo, data_tag]
                list_3 = dict(zip(fieldnames, list_2))
                writer.writerow(list_3)
                print("写入第" + str(i) + "行数据")
                i += 1
                if i > len(self.elements['houseInfo']):
                    break

# def qingxi_data_houseInfo(self, index):  # 清洗数据

# self.xpath_houseInfo()
# self.xpath_title()
# self.xpath_positionInfo()
# self.xpath_totalPrice()
# self.xpath_unitPrice()
# self.xpath_followInfo()
# self.xpath_tag()
# get_houseInfo = self.xpath_houseInfo()
# get_title = self.xpath_title()
# get_positionInfo = self.xpath_positionInfo()
# get_totalPrice = self.xpath_totalPrice()
# get_unitPrice = self.xpath_unitPrice()
# get_followInfo = self.xpath_followInfo()
# get_tag = self.xpath_tag()
# i = 1
# k = int(str(index / 5).split(".")[0])
# with open("../data/lanzhou" + str(k) + ".csv", "a", newline="", encoding="utf-8-sig") as f:
#     fieldnames = ['houseInfo', 'title', 'positionInfo', 'totalPrice/万元', 'unitPrice', 'followInfo', 'tag']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)  # 写入表头
#     writer.writeheader()
#     while True:
#         data_houseInfo = next(get_houseInfo)
#         data_title = next(get_title)
#         data_positionInfo = next(get_positionInfo)
#         data_totalPrice = next(get_totalPrice)
#         data_unitPrice = next(get_unitPrice)
#         data_followInfo = next(get_followInfo)
#         data_tag = next(get_tag)
#         list_2 = [data_houseInfo, data_title, data_positionInfo, data_totalPrice, data_unitPrice,
#                   data_followInfo, data_tag]
#         list_3 = dict(zip(fieldnames, list_2))
#         writer.writerow(list_3)
#         print("写入第" + str(i) + "行数据")
#         i += 1
#         if i > len(self.houseInfo):
#             break

# def xpath_houseInfo(self):
#     for i in xrange(len(self.houseInfo)):
#         yield self.houseInfo[i]

# def xpath_title(self):
#     for i in xrange(len(self.title)):
#         yield self.title[i]
#
# def xpath_positionInfo(self):
#     for i in xrange(len(self.positionInfo)):
#         yield self.positionInfo[i]
#
# def xpath_totalPrice(self):
#     for i in xrange(len(self.totalPrice)):
#         yield self.totalPrice[i]
#
# def xpath_unitPrice(self):
#     for i in xrange(len(self.unitPrice)):
#         yield self.unitPrice[i]
#
# def xpath_followInfo(self):
#     for i in xrange(len(self.followInfo)):
#         yield self.container.followInfo[i]
#
# def xpath_tag(self):
#     for i in xrange(len(self.tag)):
#         yield self.tag[i]
