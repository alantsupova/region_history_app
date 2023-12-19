FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY regional_history /regional_history
WORKDIR /regional_history
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password app-user

USER app-user
