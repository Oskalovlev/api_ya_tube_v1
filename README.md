# Проект «API для Yatube»

### Описание
Этот REST API построен на основе [Django REST Framework](https://www.django-rest-framework.org/)(известного как DRF). 
Вам понадобятся хотя бы фундаментальные знания о DRF, чтобы заняться разработкой этого проекта.

### Технологии
```sh
-Python 3.7
-Django==3.2.16
-DRF
-JWT
-Djoser
```

### Установка:

```sh
# клонируем репозиторий
$ git clone https://github.com/Oskalovlev/api_final_yatube.git

# зайдите в рабочий каталог - api
$ cd api

# устанавливаем требования
$ python -m pip install -r requirements.txt
```

### Запуск проекта:

```sh
# распространять модули
$ python manage.py migrate

# в корне каталога проекта..
$ python manage.py runserver
```

*PS Пожалуйста, используйте `python` вместо `python3` , если вы работаете в системе Windows*

Запустите браузер и введите [ 127.0.0.1:8000 ](http://127.0.0.1:8000/) введите в качестве
целевого URL-адреса и нажмите return.

Теперь вы можете протестировать API через интерфейс браузера DRF!

Автор: Лев Бессонов
