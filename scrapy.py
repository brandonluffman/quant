import requests 
from bs4 import BeautifulSoup
import certifi

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
#     'Accept-Language': 'da, en-gb, en',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
# }


# # url = 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html'
# url = 'https://usinflationcalculator.com/inflation/historical-inflation-rates/'
# html = requests.get(url, headers=headers, verify=False)
# html.raise_for_status()  # Raise HTTP errors if any
# soup = BeautifulSoup(html.text, 'html.parser')
# table = soup.find_all('table')  # Adjust class as needed


# # Assuming the first table is the one you want
# if table:
#     tr = table[0].find_all('tr')

#     for t in tr:
#         tds = t.find_all('td')
#         # Check if there are at least 4 `td` elements
#         if len(tds) >= 12:
#             # Print the 4th `td` element
#             print(tds[12].text)
# else:
#     print("No table found.")


stockData = [
-1.54, 34.11, 20.26, 31.01, 26.67, 19.53, -10.14, -13.04, -23.37, 26.38,
8.99, 3.00, 13.62, 3.53, -38.49, 23.45, 12.78, 0.00, 13.41, 29.60,
11.39, -0.73, 9.54, 19.42, -6.24, 28.88, 16.26, 26.89, -19.44, 24.23, 15.13
];

bondData = [
-8.04, 23.48, 1.43, 9.94, 14.92,-8.25, 16.66, 5.57, 15.12, 0.38,
4.49, 2.87, 1.96, 10.21, 20.10, -11.12, 8.46, 16.04, 2.97, -9.10,
10.75, 1.28, 0.69, 2.80, -0.02, 9.64, 11.33, -4.42, -17.83, 3.88, 15.13
];

reData = [
2.52, 1.79, 2.43, 4.02, 6.44, 7.68, 9.29, 6.68, 9.56, 9.81,
13.64, 13.51, 1.73, -5.40, -12.00, -3.86, -4.11, -3.89, 6.44, 10.71,
4.51, 5.20, 5.30, 6.21, 4.52, 3.69, 10.43, 18.87, 5.67, 6.29
]

goldData = [
-2.17, 0.98, -4.59, -21.41, -0.83, 0.85, -5.44, 0.75, 25.57, 19.89,
4.65, 17.77, 23.20, 31.92, 4.32, 25.04, 29.24, 12.02, 5.68, -27.61,
0.12, -12.11, 8.10, 12.66, -0.93, 19.08, 24.17, -3.75, 0.55, 13.26
]

averages = [
-2.6, -2.8, -3.0, -2.3, -1.6, -2.2, -3.4, -2.8, -1.6, -2.3,
-2.7, -3.4, -3.2, -2.8, -3.8, 0.4, -1.6, -3.2, -2.1, -1.5,
-1.6, -0.1, -1.3, -2.1, -2.4, -1.8, -1.2, -4.7, -8.0, -4.1
]
alll = [stockData, bondData, reData, goldData, averages]

for a in alll:
    avg = sum(a)/len(a)
    cum = sum(a)
    print('Average', avg)
    print('Cumulative', cum)