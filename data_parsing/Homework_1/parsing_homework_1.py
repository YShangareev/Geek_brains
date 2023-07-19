import requests
import json
import os

'''Task_1'''
user = 'YShangareev'
url = f'https://api.github.com/users/{user}/repos'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
s = requests.Session()
rs = s.get(url, headers=headers)

data = rs.json()
with open('json_github.json', 'w') as f:
    json.dump(data, f)

names_repo = [repo['name'] for repo in data]

print(names_repo)

'''Task_2'''
# Получим access_token при помощи переменной среды
access_token = os.environ['access_token']
# Подставим его в url и добавим полное отображение информации по группам
url_2 = f'https://api.vk.com/method/groups.get?v=5.131&access_token={access_token}&extended=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

rs = requests.get(url_2, headers=headers)

data = rs.json()

with open('json_vk.json', 'w') as f:
    json.dump(data, f)

names_groups = [items['name'] for items in data['response']['items']]
print(names_groups)
# выведем список групп так как access_token действует сутки и он скрыт
my_groups_list = ['MARVEL/DC', 'Карьера в Сбере', 'Горящие туры', 'Программирование / itProger', 'GeekBrains',
                  '#SimpleCode', 'machine learrrning', 'Московская биржа. Карьера', 'VK Чекбэк', 'Импровизация', 'M']
