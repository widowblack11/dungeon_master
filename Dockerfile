FROM python:3.10-alpine

# Копирование исходного кода автотестов в образ
COPY . .
RUN apk add git
RUN pip3 install -r requirements.txt

# Запуск автотестов
CMD pytest /tests