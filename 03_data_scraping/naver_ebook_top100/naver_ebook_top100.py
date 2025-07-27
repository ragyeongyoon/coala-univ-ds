# 네이버 시리즈 eBook TOP 100 크롤링

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 6):
    url = f'https://series.naver.com/ebook/top100List.nhn?page={page}'
    raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    code = BeautifulSoup(raw.text, 'html.parser')
    container = code.select('ul.lst_thum > li')

    for book in container:
        rank = book.select_one('span.num').text
        title = book.select_one('a > strong').text
        author = book.select_one('span.writer').text
        print('{0}위: {1}의 {2}'.format(rank, author, title))

        detail_url = 'https://series.naver.com' + book.select_one('a').get('href')

        data.append({
            '순위': rank,
            '제목': title,
            '작가': author,
            '링크': detail_url
        })

# DataFrame으로 변환 후 엑셀 저장
df = pd.DataFrame(data)
df.to_excel('naver_ebook_top100.xlsx', index=False)