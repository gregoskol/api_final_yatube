# API Yatube
## _Проект для обмена данными с сервисом Yatube через API_
## Запуск проекта:
1. Клонируйте репозиторий, перейдите в него:
```sh
git clone https://github.com/gregoskol/api_final_yatube
cd api_final_yatube
```
2. Создайте и активируйте виртуальное окружение:
```sh
python -m venv venv
source venv/Scripts/activate
```
3. Установите зависимости:
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Перейдите в папку yatube_api, выполните миграции, запустите проект:
```sh
cd yatube_api
python manage.py migrate
python manage.py runserver
```
5. После запуска можно ознакомиться с документацией API по адресу:
```sh
http://127.0.0.1:8000/redoc/
```
