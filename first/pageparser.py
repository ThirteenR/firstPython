from bs4 import BeautifulSoup


class parser:
    content = ''
    bs = ''

    def __init__(self, content):
        print('\nparser init...')
        self.content = content
        self.bs = BeautifulSoup(self.content, 'html.parser', from_encoding='utf8')

