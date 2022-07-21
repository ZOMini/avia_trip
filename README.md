[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://176.195.196.126:9000/)
![example workflow](https://github.com/zomini/avia_trip/actions/workflows/main.yml/badge.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
# Avia_trip
- Пет проект. Avia trip - база данных авиаперелетов. В разработке.
- Проект работает: http://176.195.196.126:9000/admin/ (ee-2@ya.ru / Vitaliya)
-    в requests.http тестирование API
- (Проект для отработки навыков работы с DRF.)

Взаимодействие с БД возможно через:
- Django стандартную админ панель.
- Веб интерфейс.
- API интерфейс.
 
## Стек
- Python 3.9
- Django 4.0
- Django REST framework 3.13
- Drf_yasg 1.2 (ReDoc + Swagger) API documentation http://176.195.196.126:9000/api/redoc/
- Postgres 13.0

## Info
- Для аутентификацию используем стандартный модуль DRF - Authtoken
- Для тестирования использовал REST Client for Visual Studio Code, см. файл requests.http в папке с проектом.
- Добавил автотесты API - Unit test(django)
- Добавил фильтры и поиск в API