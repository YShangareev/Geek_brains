# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
import numpy as np
import mysql.connector


class JobparserPipeline:
    def process_item(self, item, spider):
        if 'salary' in item:
            salary = item['salary']
            min_salary, max_salary, currency = self.extract_salary(salary)

            item['min_salary'] = min_salary
            item['max_salary'] = max_salary
            item['currency'] = currency

            del item['salary']

        experience = item['experience']
        experience_str = self.convert_experience(experience)
        item['experience'] = experience_str

        return item

    def extract_salary(self, salary_list):
        salary_str = ''.join(salary_list)
        min_salary = None
        max_salary = None
        currency = None
        if salary_str:
            salary_str = re.sub(r'\xa0', '', salary_str)
            salary_str = salary_str.strip()
            matches = re.findall(r'\d+|[$€£¥₽]', salary_str)
            if len(matches) == 2 and salary_str.startswith('от'):
                min_salary = int(matches[0])
                currency = matches[1]
            elif len(matches) == 2 and salary_str.startswith('до'):
                max_salary = int(matches[0])
                currency = matches[1]
            elif len(matches) == 3:
                min_salary = int(matches[0])
                max_salary = int(matches[1])
                currency = matches[2]
        return min_salary, max_salary, currency

    def convert_experience(self, experience):
        return ' '.join(experience)


class MySQLPipeline:
    def __init__(self, mysql_host, mysql_user, mysql_password, mysql_db):
        self.mysql_host = mysql_host
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_db = mysql_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mysql_host=crawler.settings.get('MYSQL_HOST'), mysql_user=crawler.settings.get('MYSQL_USER'),
                   mysql_password=crawler.settings.get('MYSQL_PASSWORD'), mysql_db=crawler.settings.get('MYSQL_DB'))

    def open_spider(self, spider):
        self.connection = mysql.connector.connect(host=self.mysql_host, user=self.mysql_user,
                                                  password=self.mysql_password, database=self.mysql_db)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        query = '''INSERT INTO job (name, min_salary, max_salary, currency, experience, url) VALUES (%s, %s, %s, %s, %s, %s)'''
        values = (item['name'], item['min_salary'], item['max_salary'], item['currency'], item['experience'], item['url'])
        self.cursor.execute(query, values)
        self.connection.commit()
        return item
