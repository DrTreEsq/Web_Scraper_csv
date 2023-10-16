import scrapy
import os
from os.path import dirname


class ConstitutionSpider(scrapy.Spider):
    name = "constitution"
    allowed_domains = ["constitutioncenter.org"]
    start_urls = ["https://constitutioncenter.org/the-constitution/full-text"]

    def parse(self, response):
        table = None
        count = 0
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
        for row in table.xpath('//tr'):
            if count > 100:
                break
            nasa_list = []
            try:
                # This is one way of doing that
                for text in row.xpath('td//text()'):
                    if text.extract().startswith('constitution'):
                        nasa_list.append(text.extract())
                print(f"exploit id: {exploit_id} -> {nasa_list}")
                append_sql_file(exploit_id, nasa_list)
            except Exception as err:
                print(f"skipping due to: {err}")
            count += 1
            



'''
Azure/SQL - next

def append_sql_file(amendment, nasas):
    line = f"INSERT INTO exploit(exploit_id, nasas) VALUES ('{amendment}', '{str(nasas)}');\n"
    if not os.path.exists(sql_file):
        with open(sql_file, 'w') as _f:
            _f.write(line)
        return
    with open(sql_file, 'a') as _f:
        _f.write(line)


current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, 'source.html')
top_dir = dirname(dirname(dirname(current_dir)))
sql_file = os.path.join(top_dir, 'sql_files/populate.sql')


class ExploitSpider(scrapy.Spider):
    name = "exploit"
    allowed_domains = ["nasa.gov"]
    start_urls = ["https://nasa.gov/source.html"]
    # Starting with actual URLs is fine
    # start_urls = ['http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html']
    # But you can use files as well!
    # start_urls = [f"file://{url}"]


# This captures 1 CVE only, but you may have many
                exploit_id = row.xpath('td//text()')[0].extract()
                nasa_id = row.xpath('td//text()')[2].extract()
                print(f"exploit id: {exploit_id} -> {nasa_id}")
                
                
# this exploit syntax is SPECIFIC to the CVEs in cve.mitre.orh
# need to use source syntax for the html from nasa or whatever website using
# was the sql file/dir created with syntax or manually first in the terminal/GUI?             
'''