# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter
from pymongo import MongoClient


class CastoramaPipeline: 
  def __init__(self):
    client = MongoClient("mongodb://localhost:27017")
    self.mongo_base = client.newdb
  
  def process_item(self, item, spider):
    item['price'] = int(item['price'].replace(' ', ''))

    collection = self.mongo_base[spider.name]
    if collection.find_one({'name':item['name']}):
      pass
    else:
      collection.insert_one(item)
    return item

class PicsPipeline(ImagesPipeline):
  #отправление реквестов по обработанным ссылкам на фото
  def get_media_requests(self, item, info):
    for img in item['photos']:
      try:
        yield scrapy.Request(img)
      except Exception as e:
        print(e)

  #переопределение пути сохранения файлов
  def file_path(self, request, response=None, info=None, *, item):
    return f'full/{item["link"].split("/")[-2]}/{request.url.split("/")[-1]}'

  #создание информации о скачанном фото для базы данных
  def item_completed(self, results, item, info):
    if results:
      item['photos'] = [itm[1] for itm in results if itm[0]]
    return item
    