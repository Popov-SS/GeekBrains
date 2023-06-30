from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from casorama.spiders.castospider import CastospiderSpider


if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    # search = input()
    runner = CrawlerRunner(settings)
    runner.crawl(CastospiderSpider, limit=96)
    reactor.run()