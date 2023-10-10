from urllib.parse import urlparse
import validators
from bs4 import BeautifulSoup


def validator(url):
    errors = []
    if not url:
        errors.append('URL обязателен')
    if len(url) > 255:
        errors.append('URL превышает 255 символов')
    if not validators.url(url) or (validators.url(url) and errors):
        errors.append('Некорректный URL')
    return errors


def normalizer(url):
    data = urlparse(url)
    return data.scheme + '://' + data.netloc


def parse_page(page_text, max_length=255):
    checks = {}
    soup = BeautifulSoup(page_text, 'html.parser')

    h1_tag = soup.find('h1')
    checks['h1'] = h1_tag.get_text().strip() if h1_tag else ''
    checks['h1'] = checks['h1'][:max_length]

    title_tag = soup.find('title')
    checks['title'] = title_tag.string.strip() if title_tag else ''
    checks['title'] = checks['title'][:max_length]

    all_metas = soup.find_all('meta', attrs={'name': 'description'})
    if all_metas:
        checks['description'] = all_metas[0].get('content', '').strip()
        checks['description'] = checks['description'][:max_length]
    else:
        checks['description'] = ''

    return checks
