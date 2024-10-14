
# SPBGUPTD

После того как вы загрузили проект:
1. Создайте виртуальное окружение с Python 3.12 и активируйте его.
2. Загрузите библиотеки, которые указаны в файле `requirements.txt`.
3. Для запуска сервера локально на своём ПК, в терминале перейдите в папку `SPBGUPTD` и через `manage.py` активируйте сервер. В командной строке пишем `python manage.py runserver`.
4. После запуска сервера в терминале можно использовать Postman для проверки API.

## API рычаги (Запросы):

### GET
http://127.0.0.1:8000/api/students/{id}/


### GET (Весь список)
http://127.0.0.1:8000/api/students/

### POST
http://127.0.0.1:8000/api/students/

### PUT
http://127.0.0.1:8000/api/students/{id}/

### DELETE
http://127.0.0.1:8000/api/students/{id}/
