import scrapy

from .AbstratSpider import AbstratSpider

# can get data, but need parse
class BOCSpider(AbstratSpider):

    name = 'boc'

    headers={
        "referer": "https://www.bochk.com/en/investment/rates/hkdrates.html",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    def start_requests(self):
        start_url=[
            "https://www.bochk.com/whk/rates/exchangeRatesHKD/exchangeRatesHKD-input.action?lang=en"
        ]
        for url in start_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            if response.status != 200:
                raise Exception('Error connecting to URL: ' +
                                str(response.url))
            fx_table = response.xpath('(//table)[1]//tr').get()
            print("---------------------------------------------------")
            print(fx_table)
            if not fx_table:
                raise Exception("xPath for table is invalid")

        except Exception as e:
            print(e)