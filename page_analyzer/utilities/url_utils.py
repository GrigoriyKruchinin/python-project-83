from urllib.parse import urlparse
import validators


def validator(url):
    errors = []
    if not url:
        errors.append('URL обязателен')
    elif len(url) > 255:
        errors.append('URL превышает 255 символов')
    elif not validators.url(url):
        errors.append('Некорректный URL')
    return errors


def normalizer(url):
    data = urlparse(url)
    return data.scheme + '://' + data.netloc
