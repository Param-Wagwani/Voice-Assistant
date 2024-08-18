import requests
from bs4 import BeautifulSoup

def google_news_search(query):
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_google_news_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    news_blocks = soup.find_all('div', class_='SoaBEf')

    for block in news_blocks:
        title = block.find('div', class_='n0jPhd').text
        link = block.find('a')['href']
        source = block.find('span').text

        item = {
            'title': title,
            'link': link,
            'source': source
        }
        results.append(item)

    return results

def fetch_article_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text
