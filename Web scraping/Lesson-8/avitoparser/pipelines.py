# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter


class AvitoparserPipeline:
  def process_item(self, item, spider):
    item['price'] = int(item['price'])
    return item

class PicsPipeline(ImagesPipeline):
  def get_media_requests(self, item, info):
    for img in item['photos']:
      try:
        yield scrapy.Request(img)
      except Exception as e:
        print(e)

  def file_path(self, request, response=None, info=None, *, item):
    return f'full/{item["link"].split("/")[-1]}/{abs(hash(response.url))}'

  def item_completed(self, results, item, info):
    if results:
      item['photos'] = [itm[1] for itm in results if itm[0]]
    return item