# Домашнее задание к лекции «Flask»


Проект REST API (backend) для сайта объявлений.
В качестве фреймворка использован Flask .

## Документация по проекту

Для запуска проекта необходимо:

Клонировать репозиторий:

```
git clone https://github.com/mlobina/flask_api_advertisement.git
cd flask_api_advertisement
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:

`pip install -r requirements.txt`

Создать файл config.py
Cоздать базу в postgres, указать настройки подключения к БД в файле config.py по образцу:

class Configuration(object):
    DEBUG = False
   
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/adv_db'

и выполнить миграцию в консоли:  
import models
from app import db
db.create_all()

Выполнить команду в терминале:

`python run`

Перейти на соответствующий эндпоинт в соответствии с описанием API-сервиса:

`http://127.0.0.1:8082/login`
`http://127.0.0.1:8082/api/v1/user`
`http://127.0.0.1:8082/api/v1/advertisement`