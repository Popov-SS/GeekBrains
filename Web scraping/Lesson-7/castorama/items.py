# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from itemloaders.processors import MapCompose, TakeFirst, Compose

#эта функция чистит приходящие значения характеристик товара и делит их на пары ключ:значение
def get_product_params(params):
  product_params = []
  for i in params:
    product_params.append(re.sub("^\n\s*|\s+$", "", i)) 
  product_params = [i for i in product_params if i != '']
  product_params = dict(zip(product_params[::2], product_params[1::2]))
  return product_params

def clean_name(value):
  name = ''.join(value)
  name = re.sub("^\n\s*|\s+$", "", name)
  return name

def clean_list(value):
  clean_list = []
  for i in value:
    clean_list.append(re.sub("^\n\s*|\s+$", "", i))
  return clean_list

#прежде чем скачивать фото, к ним нужно добавить префикс сайта для получения полной прямой ссылки
def get_photos_list(photos_list):
  photos_to_download = []
  for photo in photos_list:
    if photo.startswith('/'):
      photo = 'https://www.castorama.ru' + photo
      photos_to_download.append(photo)
    else:
      photos_to_download.append(photo)
  return photos_to_download 

class CastoramaItem(scrapy.Item):
  _id = scrapy.Field()
  name = scrapy.Field(input_processor=Compose(clean_name), output_processor=TakeFirst())
  link = scrapy.Field(output_processor=TakeFirst())
  price = scrapy.Field(output_processor=TakeFirst())
  photos = scrapy.Field(input_processor=Compose(get_photos_list))
  parameters = scrapy.Field(input_processor=Compose(get_product_params))
