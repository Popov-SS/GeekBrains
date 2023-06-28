from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from jobscraper.spiders.hhru import HhruSpider
from jobscraper.spiders.sjru import SjruSpider

if __name__ == '__main__':
  configure_logging()
  settings = get_project_settings()

  runner = CrawlerRunner(settings)
  runner.crawl(HhruSpider)
  runner.crawl(SjruSpider)
  t = runner.join()
  t.addBoth(lambda _: reactor.stop())
  reactor.run()
