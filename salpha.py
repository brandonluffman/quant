import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import random

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'da, en-gb, en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}



### Motley Fool ####
# url = 'https://archive.is/20240503012523/https://seekingalpha.com/article/4688870-apple-inc-aapl-q2-2024-earnings-call-transcript#selection-2747.62-2747.66'
url = 'https://seekingalpha.com/article/4688870-apple-inc-aapl-q2-2024-earnings-call-transcript'
html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.text)
# article = soup.find('div', class_="paywall-full-content")

# p_tags = article.find_all('p')

# lst = [p.text for p in p_tags]

# print(lst)

# ps = [p.find('strong') for p in p_tags if p.find('strong') != None]
# pse = [p for p in ps if len(p.text.split()) == 2 or p.text == 'Operator']
# psse = [p.text for p in pse]
# dialogue = [p.parent.find_next('p').text for p in pse]

# lst = list(zip(psse, dialogue))
# print(lst)

# for l in lst:
#     print(l[0])
#     print(l[1])
#     if l[1] == '[Operator signoff]':
#         break