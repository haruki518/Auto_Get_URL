 # coding: utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.set_window_size(1024,768)
driver.get('http://www.boredpanda.com/')

time.sleep(2)


article_elements = driver.find_elements_by_tag_name('article')

meta_info_list = [{
    'title': article.find_element_by_xpath('.//article/h2').text,
    'share count': article.find_element_by_xpath('.//footer/div/a/span').text,
    'points': article.find_element_by_xpath('.//footer/div[2]/div[1]/div[3]').text
} for article in article_elements]

for list in meta_info_list:
    print(list)