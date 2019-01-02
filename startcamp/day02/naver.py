import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('.ah_k')
for i in result:
    print(i.text)