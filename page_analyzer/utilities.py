from urllib.parse import urlparse
import validators
from bs4 import BeautifulSoup


def validator(url):
    errors = []
    if not url:
        errors.append('URL обязателен')
    if len(url) > 255:
        errors.append('URL превышает 255 символов')
    if not validators.url(url):
        errors.append('Некорректный URL')
    return errors


def normalizer(url):
    data = urlparse(url)
    return data.scheme + '://' + data.netloc


def parse_page(page_text):
    checks = {}
    soup = BeautifulSoup(page_text, 'html.parser')
    h1_tag = soup.find('h1')
    checks['h1'] = h1_tag.get_text().strip() if h1_tag else ''
    checks['title'] = soup.title.string if soup.title else ''
    all_metas = soup.find_all('meta')
    for meta in all_metas:
        if meta.get('name') == 'description':
            checks['description'] = meta.get('content', '')
    return checks
