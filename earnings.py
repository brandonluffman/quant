import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
import time
from tickerlist import tickers

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'da, en-gb, en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

for ticker in tickers[:5]:
    url = f'https://www.fool.com/quote/nasdaq/{ticker.lower()}'
    print(url)

    html = requests.get(url, headers=headers)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.text)

    h2 = soup.find('h2', text="Earnings Transcripts")

    time.sleep(5)

    print(h2)
