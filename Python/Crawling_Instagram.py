from selenium import webdriver
from bs4 import BeautifulSoup
import time, os
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.keys import Keys

# link
link = 'https://www.instagram.com/sejinming/'

# uid, password
uid = 'bwjubrother@gmail.com'
password = 'kjh94130!!'

# keyword
keyword = 'sejinming'

# if you need scroll
scroll_cnt = 2

# download chrome driver https://sites.google.com/a/chromium.org/chromedriver/home
driver = webdriver.Chrome(r'C:\Users\김주형\Downloads\chromedriver_win32\chromedriver')
driver.get(link)
time.sleep(1)

os.makedirs('result', exist_ok=True)

'''
### if link = 'https://www.instagram.com/'
# login
log_uid = driver.find_element_by_name('username')
log_uid.send_keys(uid)
log_password = driver.find_element_by_name('password')
log_password.send_keys(password)
log_password.send_keys(Keys.RETURN)
time.sleep(3)

# search
search = driver.find_element_by_css_selector('input.XTCLo.x3qfX')
# search = driver.find_element_by_class_name('XTCLo x3qfX')
# search = driver.find_element_by_css_selector("input[class='XTCLo x3qfX']")
search.send_keys(keyword)
log_password.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element_by_css_selector('a.yCE8d.JvDyy').click()
time.sleep(3)
'''

for i in range(scroll_cnt):
    # scroll to bottom
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)

    # click 'Load more' button, if exists
    # try:
    #     load_more = driver.find_element_by_xpath('//*[contains(@class,"U26fgb O0WRkf oG5Srb C0oVfc n9lfJ")]').click()
    # except:
    #     print('Cannot find load more button...')

# get containers
articles = driver.find_element_by_class_name('FFVAD').get_attribute('src')

print(articles)