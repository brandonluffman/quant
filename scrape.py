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

url = 'https://www.fool.com/earnings/call-transcripts/2023/02/02/apple-aapl-q1-2023-earnings-call-transcript/'

html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')

article = soup.find('div', class_ = "article-body")

p_tags = article.find_all('p')

ps = [p.find('strong') for p in p_tags if p.find('strong') != None]
pse = [p for p in ps if len(p.text.split()) == 2 or p.text == 'Operator']
psse = [p.text for p in pse]
dialogue = [p.parent.find_next('p').text for p in pse]
# print(pse)
# print(dialogue)


# l1 = []
# l2 = []
# i = 0
# for t in text:
#     if i % 2 == 0:
#         l1.append(t)
#     else:
#         l2.append(t)
    
#     i+=1

lst = list(zip(psse, dialogue))
# print(lst)

for l in lst:
    print(l[0])
    print(l[1])