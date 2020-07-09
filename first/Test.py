from first import getPageContent
from first import pageparser

request = getPageContent.getcontent()
html = request.simplerequest()
request.headerrequest()
request.cookierequest()

print(html)
parser = pageparser.parser(html)
links = parser.bs.find_all('a')
for link in links:
    print(link.get_text().strip())
