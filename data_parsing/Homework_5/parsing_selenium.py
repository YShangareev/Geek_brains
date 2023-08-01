import pandas as pd
import time
import re
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# options.add_argument('--headless')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(executable_path='./chromedriver-win64'), options=options)

driver.get('https://jsprav.ru/')


def get_data_of_city(link_href, city_name):
    informations_of_city = []
    driver.get(link_href)
    for i in range(25):
        block_of_service = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//dl[@class='cat-tile__blc-list']")))
        block = block_of_service[i]
        time.sleep(1)
        elements_of_links = block.find_elements(By.CSS_SELECTOR, 'a.cat-tile__blc-list-link')
        links = [link.get_attribute('href') for link in elements_of_links]
        for j in range(len(links)):
            link_href = links[j]
            driver.get(link_href)
            try:
                string = driver.find_element(By.XPATH, "//div[@class='cat-benefits cat-benefits-nm']/ul/li").text
                count = re.search(r'\d+', string).group()
            except NoSuchElementException:
                continue

            while True:
                company_name = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.company-info-name-org')))
                if len(company_name) == int(count):
                    break
                try:
                    next_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.company-list-next-link')))
                    next_button.click()
                except NoSuchElementException:
                    break
                time.sleep(0.5)

            company_names = driver.find_elements(By.CSS_SELECTOR, 'span.company-info-name-org')
            addresses = driver.find_elements(By.CSS_SELECTOR, 'address.company-info-address-full')
            information_of_company = [{'Название компании': name.text, 'Адрес': address.text} for name, address in
                                      zip(company_names, addresses)]
            informations_of_city.extend(information_of_company)
            time.sleep(1)
            driver.back()
        time.sleep(1)

    return city_name, informations_of_city


links_of_city = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
    (By.XPATH, "//ul[contains(@class,'cities-list_general_active')]//a[@class='cities-list__i-name']")))

informations_of_cities = {}
for link in links_of_city:
    link_href = link.get_attribute('href')
    city_name = link.text
    city_name, informations_of_city = get_data_of_city(link_href, city_name)
    informations_of_cities[city_name] = informations_of_city

df = pd.DataFrame(informations_of_cities)
df.to_excel('data_parsed.xlsx', index=False)
