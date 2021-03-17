# 네이버 api를 통한 원하는 주식의 일자별 종가, 전일비, 시가, 고가, 저가, 거래량 데이터 수집

import pandas as pd
import numpy as np
from tabulate import tabulate

import requests
from bs4 import BeautifulSoup

# 회사명, 종목코드 받아오기 - krx 사용
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
# print(code_df.head)

# 코드를 통해 주가 정보 받아오기 - 네이버 주식 사용
vari = pd.DataFrame(columns=['종목', '변동성'])
accum_profit = pd.DataFrame(columns=['종목', '누적수익률'])
risk_adj = pd.DataFrame(columns=['종목', '위험조정수익률'])

# for cnt in range(len(code_df)):
for cnt in range(1):
    code = code_df.loc[cnt, 'code']
    print(code)
    url = 'https://finance.naver.com/item/sise_day.nhn?code=' + code

    # 일자 데이터를 담을 df라는 DataFrame 정의
    df = pd.DataFrame()
    print(url)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.text, features='lxml')
    print(bs_obj)

    page_cnt = str(bs_obj.find('td', {'class': 'pgRR'}))
    start_idx = page_cnt.find('page') + 5
    end_idx = page_cnt.find('맨뒤') - 2

    try:
        end_page = int(page_cnt[start_idx:end_idx])
    except ValueError:
        pass
    

    # continue
    # 1페이지에서 26페이지(대략 1년)의 데이터만 가져오기
    end_page = end_page if end_page <26 else 26
    for page in range(1, end_page):
        pg_url = '{url}&page={page}'.format(url=url, page=page)
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
        
    # df.dropna()를 이용해 결측값 있는 행 제거
    df = df.dropna()

    # 한글로 된 컬럼명을 영어로 바꿔줌
    df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})

    # 데이터의 타입을 int형으로 바꿔줌
    df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)

    # 컬럼명 'date'의 타입을 date로 바꿔줌
    df['date'] = pd.to_datetime(df['date'])

    print(tabulate(df, headers='keys', tablefmt='psql'))

    # df.to_csv('./FinancePrice.csv')

    # price = pd.read_csv('FinancePrice.csv')
    price = df['close']
    # print(price)

    price_profit = price.pct_change()
    # print(price_profit)

    # 변동성
    price_variability = price_profit.std() * np.sqrt(len(df))
    print(price_variability)
    vari.loc[cnt, ['종목']] = item_name
    vari.loc[cnt, ['변동성']] = price_variability

    
vari = vari.sort_values(by=["변동성"], ascending=[True])


df_records = vari.to_dict('records')

print(df_records)

# model_instances = [LowVariability(
#     name=record['종목'],
#     variability=record['변동성'],
# ) for record in df_records]

# LowVariability.objects.all().delete()
# LowVariability.objects.bulk_create(model_instances)