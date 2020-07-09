from QYspider.lianjia_spider import lianjia_spider
from QYspider.xpath_parser import xpath_parser

if __name__ == "__main__":
    lanjia = lianjia_spider()
    # xpath 解析规则
    conductor = {
        'houseInfo': '//div[@class="houseInfo"]/text()',
        'title': '//div[@class="title"]/a/text()',
        'positionInfo': '//div[@class="positionInfo"]/a/text()',
        'totalPrice': '//div[@class="totalPrice"]/span/text()',
        'unitPrice': '//div[@class="unitPrice"]/span/text()',
        'followInfo': '//div[@class="followInfo"]/text()',
        'tag': '//div[@class="tag"]/span/text()'
    }
    lanjia.execute(xpath_parser(conductor))
    # container.houseInfo = html.xpath('//div[@class="houseInfo"]/text()')
    # container.title = html.xpath('//div[@class="title"]/a/text()')
    # container.positionInfo = html.xpath('//div[@class="positionInfo"]/a/text()')
    # container.totalPrice = html.xpath('//div[@class="totalPrice"]/span/text()')
    # container.unitPrice = html.xpath('//div[@class="unitPrice"]/span/text()')
    # container.followInfo = html.xpath('//div[@class="followInfo"]/text()')
    # container.tag = html.xpath('//div[@class="tag"]/span/text()')
