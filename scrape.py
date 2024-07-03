import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
import os
# from tickerlist import tickers
import time 
import csv
from etf_tickers import tickers
### Motley Fool ####
# url = 'https://www.fool.com/earnings/call-transcripts/2023/02/02/apple-aapl-q1-2023-earnings-call-transcript/'
# url = 'https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/'
# url = 'https://www.cfr.org/global-conflict-tracker'
# url = 'https://www.tradingview.com/symbols/OTC-IPCIF/'

# with open('missing_tickers.txt', 'r') as file:
#     lines = file.readlines()
#     tickers = [line.strip().replace('-', '') for line in lines]

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'da, en-gb, en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

def image_source(url):
    try:
        html = requests.get(url, headers=headers)
        html.raise_for_status()  # Raise HTTP errors if any
        soup = BeautifulSoup(html.text, 'html.parser')
        img = soup.find('img', class_='tv-circle-logo-PsAlMQQF')  # Adjust class as needed
        if img:
            img_src = img['src']
            print(img_src)
            return img_src
        else:
            return None
    except Exception as e:
        print(f'\nError fetching image source from {url}: {e}\n')
        return None


def download_image(url, save_path):
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f'\nImage successfully downloaded: {save_path}\n')
    except Exception as e:
        print(f'Error: {e}')


print(len(tickers))
# with open('indices.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip the header row
#     tickers = [row[0] for row in reader]
#     # print(tickers)


for i, ticker in enumerate(tickers):
    url = f'https://www.tradingview.com/symbols/{ticker}'
    print(f'\nPreparing to retrive img src... with url: {url}\n')
    new_img_src = image_source(url)
    if new_img_src:
        save_path = f'./etf_images/{ticker}.svg'
        download_image(new_img_src, save_path=save_path)
    if i % 5 == 0:
        time.sleep(1)
    print(f'Downloaded Ticker {ticker}, {len(tickers) - i} Left')




# df = pd.read_html(str(table))[0]

# df.to_csv('consumer_price_index_historical_data.csv', index=False)
# print(df)

# article = soup.find('div', class_ = "article-body")

# p_tags = article.find_all('p')

# ps = [p.find('strong') for p in p_tags if p.find('strong') != None]
# pse = [p for p in ps if len(p.text.split()) == 2 or p.text == 'Operator']
# psse = [p.text for p in pse]
# dialogue = [p.parent.find_next('p').text for p in pse]

# lst = list(zip(psse, dialogue))
# # print(lst)

# for l in lst:
#     print(l[0])
#     print(l[1])
#     if l[1] == '[Operator signoff]':
#         break