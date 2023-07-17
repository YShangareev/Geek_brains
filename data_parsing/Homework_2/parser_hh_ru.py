from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
import re


def convert_salary(string):
    string = string.replace(' ', '')
    string = re.sub(r'\u202f', '', string)
    string_to_list = string.split('–')
    index_number = re.search(r'\d+', string_to_list[-1][::-1])
    min_value = np.nan
    max_value = np.nan
    currency = re.search(r'\D*$', string_to_list[-1]).group(0)
    if len(string_to_list) == 2:
        min_value = int(string_to_list[0])
        max_value = int(index_number.group(0)[::-1])
    elif string_to_list[0].startswith('от'):
        min_value = int(index_number.group(0)[::-1])
    elif string_to_list[0].startswith('до'):
        max_value = int(index_number.group(0)[::-1])
    return min_value, max_value, currency


url = 'https://hh.ru/search/vacancy'
session = requests.Session()
specialization = input('Введите специальность, по которой искать вакансии: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
params = {'text': specialization,
          'page': 0}

dict_values = {'Название вакансии': [],
               'Ссылка на вакансию': [],
               'Минимальная зарплата': [],
               'Максимальная зарплата': [],
               'Валюта для расчета зарплаты': [],
               'Название компании': [],
               'Город': [],
               'Требуемый опыт': []}

while True:
    rs = session.get(url, headers=headers, params=params)
    if rs.status_code == 404:
        break
    soup = bs(rs.content, 'lxml')
    if soup.find('h1', {'data-qa': 'bloko-header-3'}).text == f'По запросу «{params["text"]}» ничего не найдено':
        print(f'По запросу «{params["text"]}» ничего не найдено')
        break
    else:
        vacancies = soup.select('div.serp-item')
        for vacancy in vacancies:
            info_vacancy = vacancy.select_one('a.serp-item__title')
            name_vacancy = info_vacancy.text
            link_of_vacancy = info_vacancy.get('href')
            try:
                salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text
                min_value, max_value, curr = convert_salary(salary)
            except AttributeError:
                min_value, max_value, curr = np.nan, np.nan, np.nan
            try:
                employer = vacancy.select_one('a.bloko-link_kind-tertiary').text
            except AttributeError:
                employer = np.nan
            city = vacancy.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
            experience = vacancy.find('div', {'data-qa': 'vacancy-serp__vacancy-work-experience'}).text
            dict_values['Название вакансии'].append(name_vacancy)
            dict_values['Ссылка на вакансию'].append(link_of_vacancy)
            dict_values['Минимальная зарплата'].append(min_value)
            dict_values['Максимальная зарплата'].append(max_value)
            dict_values['Валюта для расчета зарплаты'].append(curr)
            dict_values['Название компании'].append(employer)
            dict_values['Город'].append(city.replace(',', ''))
            dict_values['Требуемый опыт'].append(experience)
        params['page'] += 1

df = pd.DataFrame(dict_values)
df.to_excel('homework_2.xlsx', na_rep='nan', index=False)
