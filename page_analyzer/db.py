from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor
from datetime import datetime
import os


load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


def add_url_into_db(url):
    query = 'INSERT INTO urls (name, created_at) VALUES (%s, %s)'
    values = (url, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with connect(DATABASE_URL) as db:
        with db.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query, values)


def get_url_by_name(url):
    query = 'SELECT * FROM urls WHERE name = (%s)'
    with connect(DATABASE_URL) as db:
        with db.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query, (url,))
            data = cursor.fetchone()

    return data


def get_url_by_id(id):
    query = 'SELECT * FROM urls WHERE id = (%s)'
    with connect(DATABASE_URL) as db:
        with db.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query, (id,))
            data = cursor.fetchone()

    return data


def add_url_checks(checks):
    query = (
        'INSERT INTO url_checks '
        '(url_id, status_code, h1, title, description, created_at) '
        'VALUES (%s, %s, %s, %s, %s, %s)'
    )
    values = (
        checks.get('url_id'),
        checks.get('status_code'),
        checks.get('h1', ''),
        checks.get('title', ''),
        checks.get('description', ''),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    with connect(DATABASE_URL) as db:
        with db.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query, values)


def get_checks_by_url_id(id):
    query = 'SELECT * FROM url_checks WHERE url_id=(%s) ORDER BY id DESC'
    with connect(DATABASE_URL) as db:
        with db.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query, (id,))
            checks = cursor.fetchall()
    return checks


def get_all_urls():
    query = (
        'SELECT '
        'urls.id AS id, '
        'urls.name AS name, '
        'url_checks.created_at AS last_check, '
        'status_code '
        'FROM urls '
        'LEFT JOIN url_checks '
        'ON urls.id = url_checks.url_id '
        'AND url_checks.id = ('
        'SELECT max(id) FROM url_checks WHERE urls.id = url_checks.url_id) '
        'ORDER BY urls.id DESC;'
    )
    with connect(DATABASE_URL) as db:
        with db.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query)
            urls = cursor.fetchall()
    return urls
