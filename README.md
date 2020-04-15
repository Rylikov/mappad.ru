# mappad.ru
[![Build Status](https://travis-ci.org/bayborodin/mappad.ru.svg?branch=master)](https://travis-ci.org/bayborodin/mappad.ru)

Сервис хранения GPS треков
Позволяет зарегистрированным пользователям загружать GPS треки в различных форматах, сохранять их в личном кабинете, просматривать на карте, а также - видеть основные характеристики трека.
Сервис имеет социальную составляющую:
* Делиться GPS треками с другими пользователями (приватные и публичные GPS треки)
* Подписываться на треки других пользователей
* Оставлять коментарии к GPS треками других пользователей

В проекте используется интеграция со следующими внешними сервисами:
* OpenStreetMap
* Mapbox

## Запуск в Development режиме
```bash
export DATABASE_URI="postgresql://mappad:mappad@localhost/mappad" && export FLASK_ENV=development && export FLASK_DEBUG=1 && export export FLASK_APP=webapp && flask run
```
или через скрипт:
```bash
./run.sh
```

## Запуск Docker контейнера
```bash
docker build -t mappad:latest .
docker run --name mappad  -d -p 8000:5000 --rm -e DATABASE_URI=postgresql://mappad:q123Q123@mappad.ctixcsaspk7s.us-west-2.rds.amazonaws.com -e FLASK_DEBUG=1 -e SECRET_KEY=MySecretKey GA_ID=UA-0000000-00 mappad:latest
```

## Запуск тестов
```bash
python -m unittest discover
```
Запуск тестов в Docker контейнере:
```bash
docker build -t mappad:latest .
docker run -d --name app mappad:latest
docker ps -a
docker exec app python -m unittest discover
```
Покрытие тестами:
```bash
coverage run tests.py
coverage report
```
## Интерфейс приложения
<div align="center">
<img src="documentation/layout_2.png" width=50%>
<img src="documentation/layout_1.png" width=50%>
</div>
