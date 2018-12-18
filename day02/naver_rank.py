import requests
import bs4

response = requests.get('https://www.naver.com').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')
for item in result:
    rank = item.select_one('.ah_r').text
    keyword = item.select_one('.ah_k').text
    print(f'{rank} / {keyword}')