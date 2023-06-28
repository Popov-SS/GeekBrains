# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobscraperPipeline:
  def __init__(self):
    client = MongoClient("mongodb://localhost:27017")
    self.mongo_base = client.newdb

  def process_item(self, item, spider):
    item['name'] = item['name'][0]
    
    if spider.name == 'hhru':
      item['min_salary'], item['max_salary'], item['currency'] = self.process_salary_hh(item['salary'])
      item['_id'] = item['url'].split('?')[0].split('/')[-1] + '-hh'
    elif spider.name == 'sjru':
      item['min_salary'], item['max_salary'], item['currency'] = self.process_salary_sj(item['salary'])
      item['_id'] = item['url'].split('-')[-1].replace('.html', '') + '-sj'
    
    del item['salary']
    
    collection = self.mongo_base[spider.name]
    if collection.find_one({'_id':item['_id']}):
      pass
    else:
      collection.insert_one(item)
    return item

  def process_salary_hh(self, salary):
    if 'от ' and ' до ' in salary:
      min_salary = int(salary[1].replace('\xa0', ''))
      max_salary = int(salary[3].replace('\xa0', ''))
      currency = salary[5]
    elif 'от ' in salary:
      min_salary = int(salary[1].replace('\xa0', ''))
      max_salary = None
      currency = salary[3]
    elif 'до ' in salary:
      min_salary = None
      max_salary = int(salary[1].replace('\xa0', ''))
      currency = salary[3]
    else:
      min_salary = None
      max_salary = None
      currency = None
    return min_salary, max_salary, currency

  def process_salary_sj(self, salary):
    if 'от' in salary:
      min_salary = int(salary[2].replace('\xa0', '')[:-1])
      max_salary = None
      currency = salary[2].replace('\xa0', '')[-1]
    elif 'до' in salary:
      min_salary = None
      max_salary = int(salary[2].replace('\xa0', '')[:-1])
      currency = salary[2].replace('\xa0', '')[-1]
    elif '—' in salary:
      min_salary = int(salary[0].replace('\xa0', ''))
      max_salary = int(salary[4].replace('\xa0', ''))
      currency = salary[6]
    elif salary[0][0].isdigit():
      min_salary = int(salary[0].replace('\xa0', ''))
      max_salary = int(salary[0].replace('\xa0', ''))
      currency = salary[2]
    else:
      min_salary = None
      max_salary = None
      currency = None
    return min_salary, max_salary, currency