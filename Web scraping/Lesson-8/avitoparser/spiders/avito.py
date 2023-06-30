from scrapy import Request
import scrapy
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from avitoparser.items import AvitoparserItem


class AvitoSpider(scrapy.Spider):
  name = "avitoparser"
  allowed_domains = ["avito.ru"]
  start_urls = ["https://www.avito.ru"]

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.start_urls = [f"https://www.avito.ru/sankt-peterburg?q={kwargs.get('search')}"]

  def start_requests(self):
    if not self.start_urls and hasattr(self, "start_url"):
      raise AttributeError(
          "Crawling could not start: 'start_urls' not found "
          "or empty (but found 'start_url' attribute instead, "
          "did you miss an 's'?)"
      )
    for url in self.start_urls:
      yield SplashRequest(url)

  def parse(self, response):
    links = response.xpath("//h3[@itemprop='name']/../@href").getall()  # Извлекаем ссылку до конца
    for link in links:
      yield SplashRequest("https://avito.ru" + link, callback=self.parse_ads)

  def parse_ads(self, response):
    loader = ItemLoader(item=AvitoparserItem(), response=response)
    loader.add_xpath('name', "//h1//text()")
    loader.add_value('link', response.url)
    loader.add_xpath('price', "//span[@itemprop='price']/@content")
    loader.add_xpath('description', "//div[@data-marker='item-view/item-description']//text()")
    loader.add_xpath('photos', "//img[not(contains(@class, 'photo-slider')) and not(contains(@alt, 'метро'))]/@src")
    yield loader.load_item()
