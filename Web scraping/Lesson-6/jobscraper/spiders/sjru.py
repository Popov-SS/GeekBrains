import scrapy
from scrapy.http import HtmlResponse
from jobscraper.items import JobscraperItem


class SjruSpider(scrapy.Spider):
  name = "sjru"
  allowed_domains = ["superjob.ru"]
  start_urls = ["https://www.superjob.ru/vacancy/search/?keywords=python"]

  def parse(self, response: HtmlResponse, **kwargs):
    links = response.xpath("//div[contains(@class, 'f-test-vacancy-item')]//div/span/a[contains(@href, 'vakansii')]/@href").getall()
    for link in links:
      yield response.follow(link, callback=self.vacancy_parse)
    next_page = response.xpath("//a[@rel='next']").get()
    if next_page:
      yield response.follow(next_page, callback=self.parse)

  def vacancy_parse(self, response: HtmlResponse):
    name = response.xpath("//h1//text()").getall()
    url = response.url
    salary = response.xpath("//h1/following-sibling::span//text()").getall()
    yield JobscraperItem(name=name, url=url, salary=salary)
