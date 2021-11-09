# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code/