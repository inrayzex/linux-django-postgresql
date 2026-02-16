markdown
# Django Blog Portfolio

Простой блог на Django с PostgreSQL, Gunicorn и Nginx.  
Развёрнут на Rocky Linux 9, полностью рабочий стек.

## Стек технологий
- Python 3.9 / Django 4.2
- PostgreSQL 17
- Gunicorn + Nginx
- Rocky Linux 9

## Функциональность
- Модель Post (заголовок, текст, дата)
- Админ-панель Django
- Статика отдаётся через Nginx
- Gunicorn через Unix-сокет

## Установка (кратко)
1. Клонировать репозиторий
2. Создать виртуальное окружение
3. Установить зависимости: `pip install -r requirements.txt`
4. Настроить PostgreSQL
5. Запустить Gunicorn и Nginx

## Автор
Денис Мыцик
GitHub: [inrayzex](https://github.com/inrayzex)
