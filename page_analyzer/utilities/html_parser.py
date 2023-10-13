from bs4 import BeautifulSoup


def parse_page(content, max_length=255):
    checks = {}
    soup = BeautifulSoup(content, 'html.parser')

    h1_tag = soup.find('h1')
    checks['h1'] = h1_tag.get_text().strip() if h1_tag else ''
    checks['h1'] = checks['h1'][:max_length]

    title_tag = soup.find('title')
    checks['title'] = title_tag.string.strip() if title_tag else ''
    checks['title'] = checks['title'][:max_length]

    description_tag = soup.find('meta', attrs={'name': 'description'})
    if description_tag:
        checks['description'] = description_tag.get('content', '').strip()
        checks['description'] = checks['description'][:max_length]
    else:
        checks['description'] = ''

    return checks
