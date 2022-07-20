# Avia_trip
Пет проект. Avia trip - база данных авиаперелетов. В разработке.
(Проект для отработки навыков работы с DRF.)

Взаимодействие с БД возможно через:
- Django стандартную админ панель.
- Веб интерфейс.
- API интерфейс.
 
## Стек
- Python 3.9
- Django 4.0
- Django REST framework 3.13
- Drf_yasg 1.2 (ReDoc + Swagger) API documentation

## Info
- Для аутентификацию используем стандартный модуль DRF - Authtoken
- Для тестирования использовал REST Client for Visual Studio Code, см. файл requests.http в папке с проектом.
- Добавил автотесты API - Unit test(django)
- Добавил фильтры и поиск в API