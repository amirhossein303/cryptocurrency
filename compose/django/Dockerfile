FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/
COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements/development.txt

WORKDIR /code/cryptocurrency_project
