import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import random


with open('tenk.csv', 'r') as r:
    tenk = r.read()
    print()
urls = ['https://www.sec.gov/Archives/edgar/data/1067983/000095017023004451/brka-20221231.htm', 
        'https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm', 
        'https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm', 
        'https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm',
        'https://www.sec.gov/Archives/edgar/data/1601485/000160148523000011/angn-20221231.htm',
        'https://www.sec.gov/Archives/edgar/data/1829432/000162828023005609/aac-20221231.htm',
        'https://www.sec.gov/Archives/edgar/data/1066923/000121390023031057/f10k2022_futurefintech.htm',
        'https://www.sec.gov/Archives/edgar/data/78003/000007800323000024/pfe-20221231.htm',
        'https://www.sec.gov/Archives/edgar/data/1817640/000156459023004918/brez-10k_20221231.htm',
        'https://www.sec.gov/Archives/edgar/data/1326380/000132638023000019/gme-20230128.htm',
        'https://www.sec.gov/Archives/edgar/data/1858681/000185868123000007/apo-20221231.htm',
        'https://www.sec.gov/Archives/edgar/data/759944/000075994423000029/cfg-20221231.htm',
        'https://www.sec.gov/Archives/edgar/data/1177394/000117739424000014/snx-20231130.htm'
        ]
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'da, en-gb, en',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}


url = urls[random.randint(0,len(urls)-1)]
print(url)
html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')

balance_sheets = ['Consolidated Balance Sheets' , "Balance Sheets"]
income_statement = ['Consolidated Statements of Income', 'Consolidated Statements of Comprehensive Income', 'Consolidated Statements of Operations', 'Statements of Operations']
cash_flow_statement = ['Consolidated Statements of Cash Flows']

bs_ids = ['balance_sheets']
is_ids = ['consolidated_statements_income','consolidated_statements_comprehensive_in', 'consolidated_statements_earnings']

pattern = re.compile('|'.join(map(re.escape, income_statement)), re.IGNORECASE)


if soup.find_all('a', text=pattern):
    anchors = soup.find_all('a', text=pattern)
    for a in anchors:
        if pattern.match(a.text):
            a_id = a.get('id')
            print('id:', a_id)
        else:
            print('No ID')

    if soup.find(id=a_id):
        ele = soup.find(id=a_id)
        table = ele.find_next('table')
        print('Found table')
    else:
        print('No Element')


tr = table.find_all('tr')

lst = []
for td in tr:
    cur_row = []
    for t in td.find_all('td'):
        if t.text != "$":
            cur_row.append(t.text)
    lst.append(cur_row)

df = pd.DataFrame(lst)
df.to_csv('data4.csv', index="False")

# if soup.find(id=bs_ids[0]):
#     bs = soup.find(id=bs_ids[0])
#     if bs.find_next('table'):
#         table = bs.find_next('table')
# if soup.find(id=is_ids[0]):
#     bs = soup.find(id=is_ids[0])
#     if bs.find_next('table'):
#         table = bs.find_next('table')
# elif soup.find('a', text=pattern):
#     anchor = soup.find_all('a', text=pattern)
#     for a in anchor:
#         print(a)
#         if pattern.match(a.text):
#             anchor_tag = a.get('id')
#             anchor = soup.find(id=anchor_tag)
#             # print(anchor)
#             table = anchor.find_next('table')
#             print('Found table by a tag')
#         else:
#             anchor = anchor[0]
#             table = anchor.find_next('table')

# elif soup.find_all('span', text=pattern):
#     bs = soup.find_all('span', text=pattern)
#     for b in bs:
#         print(b)
#         if pattern.match(b.text.lstrip().rstrip()) and not b.find('a') and len(b.text) < 100:
#             print('Found Match')
#             print('BS:', b)
#             print('Length of string', len(b.text))
#             bs = b.parent
#     if len(bs) < 1 and bs.find_next('table'):
#         print('Found Table with no Div element')
#         table = bs.find_next('table')
#     else:
#         print(bs)
#         next_divs = bs.find_all_next('div', limit=3)
#         if next_divs:
#             for div in next_divs:
#                 if div.find('table'):
#                     table = div.find('table')
#                     print('Found table within a NEXT div element')
#                     break
#                 else:
#                     print('Div has no table')
        
#         else:
#             print("No table found following the span.")

# tr = table.find_all('tr')

# lst = []
# for td in tr:
#     cur_row = []
#     for t in td.find_all('td'):
#         if t.text != "$":
#             cur_row.append(t.text)
#     lst.append(cur_row)

# df = pd.DataFrame(lst)
# df.to_csv('data4.csv', index="False")