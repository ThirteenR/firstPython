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
    def __init__(self, **params):
        self.url = params['url']
        self.iterators = {}
        self.data_mode = params['data_mode']
        self.mode_fns = {}
        self.type = "Spider"
        self.container = dict()
        self.ps = params['ps']
        self.headers = params['headers']
        self._def_mode_init()

    # 执行爬虫的入口
    def execute(self):
        for i in xrange(1, 21):
            url_str: str = self.url.format(i)  # 构造请求url
            rsp = requests.get(url_str, headers=self.headers)
            self.container = self.ps.parse_content_rsp(rsp)
            self.data_filter()
            self.mode_fns[self.data_mode](i)  # 根据爬虫设置的数据保存模式执行指定函数

    # 加载默认的数据保持模式
    def _def_mode_init(self):
        self.mode_fns['csv'] = self._save_data_csv
        self.mode_fns['db'] = self._save_data_db

    # 自定义数据模式
    def add_mode(self, data_mode: str, mode_fn):
        self.mode_fns[data_mode] = mode_fn

    def data_filter(self):
        for k in self.container:
            print(k)
            self.iterators[k] = self.iterator(k, self.container[k])

    def iterator(self, k, content):
        for i in xrange(len(content)):
            yield self.container[k][i]

    def _save_data_db(self, page_num):
        pass

    def _save_data_csv(self, page_num):
        pass
