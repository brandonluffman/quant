from tickerlist import tickers
import requests
from bs4 import BeautifulSoup
import os
import time

def download_image(url, save_path):
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        response = requests.get(url, stream=True)

        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        # print(f'Image successfully downloaded: {save_path}')
    except Exception as e:
        print(f'Error: {e}')


# tickers = [ticker.replace('-', '') for ticker in tickers]

missing_ticker_imgs = []

with open('missing_tickers.txt', 'r') as file:
    lines = file.readlines()
    tickers = [line.strip().replace('-', '') for line in lines]
    # print(tickers)

for i, ticker in enumerate(tickers):
    url = f'https://raw.githubusercontent.com/davidepalazzo/ticker-logos/main/ticker_icons/{ticker}.png'
    
    response = requests.get(url, stream=True)
    if response.status_code == 404:
        print('Adding: ', ticker)
        missing_ticker_imgs.append(ticker)
        continue  # Continue to the next ticker in the loop
    print('Status : ', response.status_code)
    save_path = f'./images/{ticker}.png'
    download_image(url, save_path=save_path)
    if i % 5 == 0:
        time.sleep(1)
    print(f'Downloaded Ticker {ticker}, {len(tickers) - i} Left')


with open('missing_tickers-2.txt', 'w') as file:
    file.write('\n'.join(missing_ticker_imgs))
