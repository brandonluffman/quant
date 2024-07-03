import yfinance as yf
import json
from etf_tickers import tickers
import time

data = {}

ticker = 'AAPL'
ticker_data = yf.Ticker(ticker)
print(ticker_data.info)
# i = 0
# for ticker in tickers:
#     ticker_data = yf.Ticker(ticker)
#     data[ticker] = ticker_data.info
#     if i % 5 == 0:
#         time.sleep(1)
#     print(f'Finished with Ticker: {ticker} - {len(tickers)-i}')

#     i += 1
#     # print(ticker_data.info)


# with open('etf_yfin_data.json', 'w') as f:
#     json.dump(data, f, indent=4)
# print(data)