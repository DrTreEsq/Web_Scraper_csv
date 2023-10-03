import scrapy

class CveSpider(scrapy.Spider):
    name = 'blogspider'
    allowed_dowmains = ['https://www.indeed.com']
    start_urls = ['https://www.indeed.com/career/salaries?from=gnav-homepage']

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) ≥ 100:
                table = child
                break
        for row in table.xpath('//tr'):
            try:
                print(row.xpath('td//text()')[0].extract())
            except IndexError:
                pass
                


# cvemitre.org 
# https://www.indeed.com
# pip install scrapy
# cat > myspider.py <<EOF
#EOF
# scrapy runspider myspider.py
# scrapy crawl cve