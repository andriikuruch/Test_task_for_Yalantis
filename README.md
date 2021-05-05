# Test_task_for_Yalantis
Тестовое задание для Yalantis Python School.

# Развертывание проекта
Скачайте репозоторий с помощью команды ```git clone https://github.com/andriikuruch/Test_task_for_Yalantis.git```. Либо скачайте архив и разархивируйте его.

## Windows
Создайте виртуальное окружение с помощью последовательности команд:
```
py -m venv venv
.\venv\Scripts\activate.bat
```
Установите зависимости ```pip install -r requirements.txt```.

## Linux
Создайте виртуальное окружение с помощью последовательности команд:
```
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости ```pip install -r requirements.txt```.

# Запуск проекта
## Windows
Для запуска проекта используйте команду ```py manage.py runserver```. Для запуска тестов используйте команду ```py manage.py test```.

## Linux
Для запуска проекта используйте команду ```python3 manage.py runserver```. Для запуска тестов используйте команду ```python3 manage.py test```.


# Endpoints
* ```.../catalog/``` - вывод всех курсов.
* ```.../catalog?search=<title>&date_start=<date>&date_end=<date>``` - поиск курсов по названию и филтры по дате начала курса и дате конца (любой из параметров может быть опущен).
* ```.../catalog/create``` - эндпоинт для создания курса.
* ```.../catalog/course/<id>``` - эндпоинт для вывода информации, редактирования и удаления курса.
