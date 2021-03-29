import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/sise_day.nhn?code=155660'

result = requests.get(url)
bs_obj = BeautifulSoup(result.text, features='lxml')

print(bs_obj)