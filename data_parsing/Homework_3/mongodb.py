from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pprint import pprint
import pandas as pd

df = pd.read_excel('homework_2.xlsx')

dict_data = df.to_dict(orient='records')

client = MongoClient('127.0.0.1', 27017)

db = client['hh_ru']
vacancy = db['vacancy']

vacancy.create_index([('Ссылка на вакансию', 1)], unique=True)

for doc in dict_data:
    try:
        vacancy.insert_one(doc)
    except DuplicateKeyError:
        print('Данные не могут быть добавлены, повторение поля "Ссылка на вакансию"')

for doc in vacancy.find({}):
    pprint(doc)

sales_max = int(input('Введите максимальное значение зарплаты,выше которого нужно искать:'))

for doc in vacancy.find(
        {'$or': [{'Максимальная зарплата': {'$gt': sales_max}}, {'Минимальная зарплата': {'$gt': sales_max}}]}):
    print('>'*50)
    pprint(doc)

for doc in vacancy.find(
        {'$or': [{'Максимальная зарплата': {'$eq': sales_max}}, {'Минимальная зарплата': {'$eq': sales_max}}]}):
    print('='*50)
    pprint(doc)

