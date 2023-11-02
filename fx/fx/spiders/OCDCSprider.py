import scrapy
from bs4 import BeautifulSoup
from .AbstratSpider import AbstratSpider

# can get data, but need parse
class OCDCSprider(AbstratSpider):

    name = 'ocdc'

    headers={
        "referer": "https://www.bochk.com/en/investment/rates/hkdrates.html",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    start_urls = [
        "https://www.ocbcwhhk.com/whb/action/rate/whbRate.do?locale=zh-hk&id=fc_exchange_rate_gold"
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        # Assuming the tables are identified by the class 'my_table_class'
        tables = soup.find_all('table', {'class': 'my_table_class'})
        for table in tables:
            # Process each table here
            rows = table.find_all('tr')
            for row in rows:
                # Process each row here
                cols = row.find_all('td')
                for col in cols:
                    # Process each column here
                    # If there are nested tables, they will also be 'td' elements, so you can recursively call 'parse' here
                    self.parse_table(col)

    def parse_table(self, table):
        # This is a recursive function that will process nested tables
        # We'll assume that 'table' is a BeautifulSoup object representing a table
        rows = table.find_all('tr')
        for row in rows:
            # Process each row here
            cols = row.find_all('td')
            for col in cols:
                # Process each column here
                # If there are nested tables, they will also be 'td' elements, so we recursively call 'parse_table' here
                self.parse_table(col)


