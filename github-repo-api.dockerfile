FROM python:3.9.1-alpine3.12

WORKDIR /
ENV FLASK_APP=/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .