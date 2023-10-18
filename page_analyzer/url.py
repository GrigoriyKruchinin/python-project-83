from urllib.parse import urlparse
import validators


def validator(url):
    error = None
    if not url:
        error = 'URL обязателен'
    elif len(url) > 255:
        error = 'URL превышает 255 символов'
    elif not validators.url(url):
        error = 'Некорректный URL'
    return error


def normalizer(url):
    data = urlparse(url)
    return data.scheme + '://' + data.netloc
