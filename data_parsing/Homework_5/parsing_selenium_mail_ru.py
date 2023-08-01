import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# options.add_argument('--headless')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(executable_path='./chromedriver-win64'), options=options)

driver.get('https://mail.ru/')

'''Страница авторизации'''
button = driver.find_element(By.CSS_SELECTOR, 'button.resplash-btn_primary')
button.click()

driver.implicitly_wait(10)

iframe = driver.find_element(By.CSS_SELECTOR, 'iframe.ag-popup__frame__layout__iframe')
driver.switch_to.frame(iframe)

user = driver.find_element(By.NAME, 'username')
user.send_keys('study.ai_172@mail.ru')
user.send_keys(Keys.ENTER)

user = driver.find_element(By.NAME, 'password')
user.send_keys('NextPassword172#')
user.send_keys(Keys.ENTER)

driver.switch_to.default_content()

'''Собираем письма'''


def get_info(email):
    information = {}
    driver.get(email)
    time.sleep(1)
    information['Тема письма'] = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.thread-subject'))).text
    information['Отправитель'] = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.letter__author > span.letter-contact'))).text
    information['Время получения'] = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.letter__author > div.letter__date'))).text
    information['Текст письма'] = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='letter__body']"))).text
    back = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.portal-menu-element_back')))
    back.click()
    return information


def scroll():
    block = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.dataset__items')))
    driver.execute_script("arguments[0].scrollTop += 588;", block)
    curr_scroll_top = driver.execute_script("return arguments[0].scrollTop;", block)
    return curr_scroll_top


prev_scroll_top = 0
set_links = set()
while True:
    time.sleep(1)
    emails = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.llc')))
    for email in emails:
        set_links.add(email.get_attribute('href'))
    time.sleep(1)
    curr_scroll_top = scroll()
    if curr_scroll_top == prev_scroll_top:
        break
    prev_scroll_top = curr_scroll_top

mail_box = []
for link in set_links:
    time.sleep(1)
    information = get_info(link)
    mail_box.append(information)

df = pd.DataFrame(mail_box)
df.to_excel('mail_box.xlsx')

print()
