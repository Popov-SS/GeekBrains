# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from itemloaders.processors import MapCompose, TakeFirst, Compose

def clean_name(value):
  name = ''.join(value)
  name = re.sub("^\n\s*|\s+$", "", name)
  return name

def get_description(desc):
  clean_desc = []
  for i in desc:
    clean_desc.append(re.sub("^\n\s*|\s+$", "", i)) 
  clean_desc = [i for i in clean_desc if i != '']
  clean_desc = '\n'.join(clean_desc)
  return clean_desc

class AvitoparserItem(scrapy.Item):
  _id = scrapy.Field()
  name = scrapy.Field(input_processor=Compose(clean_name), output_processor=TakeFirst())
  link = scrapy.Field(output_processor=TakeFirst())
  price = scrapy.Field(output_processor=TakeFirst())
  photos = scrapy.Field()
  description = scrapy.Field(input_processor=Compose(get_description))
