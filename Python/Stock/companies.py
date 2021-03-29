import pandas as pd
import numpy as np
from tabulate import tabulate

import requests
from bs4 import BeautifulSoup


def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code.strip())
    return url


code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드', '업종', '주요제품']]


df_records = code_df.to_dict('records')

print(tabulate(df_records[:5], headers="keys", tablefmt="pretty"))