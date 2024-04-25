import requests
import fake_useragent
from fake_useragent import UserAgent
import bs4
from bs4 import BeautifulSoup
import re

def get_links(n):
    url = "https://ilibrary.ru/author/chekhov/l.all/index.html"
    news = requests.get(url + str(n))
    news_soup = BeautifulSoup(news.text, 'html.parser')
    div_articles = news_soup.find('div', attrs={'class': 'list'})
    urls = []
    if div_articles:
        urls = div_articles.find_all('p')
        urls = ['https://ilibrary.ru/' + url.find('a').get('href') for url in urls]
    return urls

all_urls = []
for i in range(1):
    all_urls += get_links(i)  

def get_html(url: str):
  html = requests.get(url, headers={"User-agent": UserAgent().chrome})
  if status_code := html.status_code != 200:
    print(f'Request error: {status_code}\n{url}')
    return None
  return html

s = ''
for j in all_urls:
  html = get_html(j)
  bs = BeautifulSoup(html.text, 'html.parser')
  content = bs.find('div', attrs={'class': 't hya'})
  if content:
    items = content.find_all('z')
  for item in items:
    s += item.get_text()
  s = re.sub(r'(\w)(\.)(\w)', r'\1\2 \3', s, flags = re.MULTILINE)
  s = re.sub(r'\s{2,}', ' ', s)
f = open(r'\частотные_словари\python\corpus.txt', 'w', encoding="utf-8")
f.write(s)
f.close