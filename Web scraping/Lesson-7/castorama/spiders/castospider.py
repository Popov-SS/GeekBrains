import scrapy
from castorama.items import CastoramaItem
from scrapy.loader import ItemLoader

class CastospiderSpider(scrapy.Spider):
  name = "castospider"
  allowed_domains = ["castorama.ru"]
  start_urls = ["https://castorama.ru"]

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.start_urls = [f"https://www.castorama.ru/tools/hand-tools/?limit={kwargs.get('limit')}"]

  def parse(self, response):
    links = response.xpath("//ul[contains(@class, 'products-grid')][1]//a[contains(@class, 'product-card__name')]")
    for link in links:
      yield response.follow(link, callback=self.tool_parse)

  def tool_parse(self, response):
    loader = ItemLoader(item=CastoramaItem(), response=response)
    loader.add_xpath('name', "//h1/text()")
    loader.add_xpath('price', "//span[@class='price']/span/span[1]//text()")
    loader.add_xpath('parameters', "//div[@class='product-block product-specifications']/dl//text()")
    #фото попадают в поля в виде списка неполных ссылок
    loader.add_xpath('photos', "//img[contains(@class, 'top-slide__img')]/@data-src")
    loader.add_value('link', response.url)
    yield loader.load_item()
    