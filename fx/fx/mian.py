from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.BOCSpider import BOCSpider
from spiders.OCDCSprider import OCDCSprider

def main():
    # Create a CrawlerProcess instance with project settings
    process = CrawlerProcess(settings=get_project_settings())

    # Add your spider to the process
    process.crawl(OCDCSprider)

    # Start the crawling process
    process.start()

if __name__ == '__main__':
    main()