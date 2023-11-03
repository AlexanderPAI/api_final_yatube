## 1. О проекте:
Yatube_api - API для учебного проекта блога Yatube.

Интерфейс позволяет взаимодействовать с проектом социанльной сети Yatube посредством отправки запросов на URL интерфейса.

## 2. Подробная документация API:

Доступна после запуска проекта - см. п.3:
http://127.0.0.1:8000/redoc/



## 3. Как запустить проект:
Клонировать репозиторий и перейти в него в терминале:
```bash
git clone https://github.com/AlexanderPAI/api_final_yatube.git
cd api_final_yatube
```
Создать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```bash
cd yatube_api
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate
```
Запустить проект:
```bash
python3 manage.py runserver
```

## Автор:
Александр Петров
https://github.com/AlexanderPAI
