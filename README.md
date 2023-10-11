# Page Analyzer
***
![Hexlet Badge](https://img.shields.io/badge/Hexlet-116EF5?logo=hexlet&logoColor=fff&style=for-the-badge)
[![Actions Status](https://github.com/GrigoriyKruchinin/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/GrigoriyKruchinin/python-project-83/actions)
[![Check_my_Actions](https://github.com/GrigoriyKruchinin/python-project-83/actions/workflows/my_workflow.yml/badge.svg)](https://github.com/GrigoriyKruchinin/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/243dd971a19c9d35615d/maintainability)](https://codeclimate.com/github/GrigoriyKruchinin/python-project-83/maintainability)

__"Page Analyzer__ - третий проект, разработанный в рамках обучения на курсе Хекслет. Это сайт, который анализирует указанные страницы на SEO-пригодность.

[Link on render.com](https://page-analyzer-dlr3.onrender.com)
***
## Перед установкой
Для установки и запуска проекта вам потребуется Python версии  3.10 и выше, инструмент для управления зависимостями Poetry и база данных PostgreSQL.

Перед началом использования проекта убедитесь, что вышеописанные утилиты установлены на вашем устройстве. В противном случае используйте официальную документацию для установки.

## Установка

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
```
git clone git@github.com:GrigoriyKruchinin/python-project-83.git
```
2. Перейдите в директорию проекта:
```
cd python-project-83
```
3. Установите необходимые зависимости с помощью Poetry:
```
poetry install
```
4. Создайте файл .env в корневой папке и добавьте в него переменные в следующем формате:

```
DATABASE_URL=postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY='{your secret key}'
```

5. Затем запустите команды из database.sql, чтобы создать необходимые таблицы.

***

## Использование
1. Для запуска сервера Flask с помощью Gunicorn выполните команду:

```
make start
```
По умолчанию сервер будет доступен по адресу http://0.0.0.0:8000.

2. Также можно запустить сервер локально в режиме разработки с активным отладчиком:

```
make dev

```
Сервер для разработки будет доступен по адресу http://127.0.0.1:5000.

Чтобы добавить новый сайт, введите его адрес в форму на главной странице. Введенный адрес будет проверен и добавлен в базу данных.

После добавления сайта можно начать его проверку. На странице каждого конкретного сайта появится кнопка, и нажав на нее, вы создадите запись в таблице проверки.

Все добавленные URL можно увидеть на странице /urls.
***
#### Способы использования
Проект можно использовать локально и онлайн (например с помощью стороннего сервиса [render.com](https://dashboard.render.com/)). Следуйте инструкциям с официального сайта для добавления веб-сервиса и онлайн базы данных. Не забывайте про использования переменных окружения.

***
## Контакты
- Автор: Grigoriy Kruchinin
- [GitHub](https://github.com/GrigoriyKruchinin)
- [Email](gkruchinin75@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/grigoriy-kruchinin/)
***
### Демонстрация работы программы:
[Демонстрация работы проекта](https://python-page-analyzer-ru.hexlet.app/)
***