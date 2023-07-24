import pandas as pd
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from pprint import pprint


# Функция парсинга Яндекс Новости
def yandex_parsing(url, driver):
    # Используем библиотеку selenium, чтобы не возникло непредвиденных ситуаций
    # так как страницы динамически подгружают данные
    driver.get(url)
    driver.implicitly_wait(10)
    # Получаем все блоки с новостями
    elements = driver.find_elements(By.XPATH,
                                    "//div[contains(@class,'mg-card') and contains(@class, ' mg-grid__item')]")
    news_list = []
    # Проходимся по каждому элементу
    for content in elements:
        news_dict = {}
        # Извлекаем Заголовок
        news_dict['Заголовок'] = content.find_element(By.XPATH, ".//h2/a").text
        # Извлекаем ссылку
        news_dict['Ссылка'] = content.find_element(By.XPATH, ".//h2/a").get_attribute('href')
        # Извлекаем Время публикации
        news_dict['Время публикации'] = content.find_element(By.XPATH,
                                                             ".//div[@class='mg-card-footer__left']//span[@class='mg-card-source__time']").text
        # Извлекаем Источник новости
        news_dict['Источник'] = content.find_element(By.XPATH,
                                                     ".//div[@class='mg-card-footer__left']//span[@class='mg-card-source__source']/a").text
        news_dict['Сервис'] = 'yandex_dzen'
        news_list.append(news_dict)
    return news_list


# Функция конвертации наших новостей в excel
def convert_excel(data, url):
    list_name_services = [re.compile('yandex'), re.compile('mail'), re.compile('lenta')]
    for service in list_name_services:
        if service.findall(url):
            df = pd.DataFrame(data)
            df.to_excel(f'news_{service.findall(url)[0]}.xlsx', index=False)


def mail_parsing(url, driver):
    # Используем библиотеку selenium, чтобы не возникло непредвиденных ситуаций
    # так как страницы динамически подгружают данные
    driver.get(url)
    driver.implicitly_wait(10)
    # Получаем все блоки с новостями
    links = driver.find_elements(By.XPATH, "//div[@class='js-module']//span[contains(@class,'js-topnews__item')]/a")
    news_list = []
    # Проходимся по каждому элементу
    for i in range(len(links)):
        links = driver.find_elements(By.XPATH, "//div[@class='js-module']//span[contains(@class,'js-topnews__item')]/a")
        link = links[i]
        news_dict = {}
        # Извлекаем ссылку
        news_dict['Ссылка'] = link.get_attribute('href')
        # Проходим по ссылке
        driver.execute_script("arguments[0].click();", link)
        # Извлекаем Заголовок
        news_dict['Заголовок'] = driver.find_element(By.XPATH, "//h1").text
        # Извлекаем Время публикации
        news_dict['Время публикации'] = driver.find_element(By.XPATH, ".//span[@datetime]").text
        # Извлекаем Источник новости
        news_dict['Источник'] = driver.find_element(By.XPATH,
                                                    ".//a[contains(@class,'breadcrumbs__link')]/span[@class = 'link__text']").text
        news_dict['Сервис'] = 'mail.ru'
        news_list.append(news_dict)
        driver.back()
    return news_list


# Задаем опции Chrome
chrome_options = Options()
# Чтобы не все операции были в фоне
chrome_options.add_argument('--headless')
path_to_driver = os.environ['path_to_driver']
# Устанавливаем наши драйвера
driver = webdriver.Chrome(service=Service(executable_path=path_to_driver), options=chrome_options)

url_yandex = 'https://yandex.ru/news/'
url_mail = 'https://news.mail.ru/'

'''Yandex'''
news_list_yandex = yandex_parsing(url_yandex, driver)
convert_excel(news_list_yandex, url_yandex)
'''Mail'''
news_list_mail = mail_parsing(url_mail, driver)
convert_excel(news_list_mail, url_mail)

news_all = news_list_mail+news_list_yandex


client = MongoClient('127.0.0.1', 27017)

db = client['news_db']
collection = db['news']
for news in news_all:
    filter_for_update = {'Ссылка': news['Ссылка']}
    collection.update_one(filter_for_update, {'$set': news}, upsert=True)

for news in collection.find({}):
    pprint(news)
