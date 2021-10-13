# syntax=docker/dockerfile:1
FROM python:3-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /opt/code
RUN apt-get update && apt-get -y --no-install-recommends install git libffi-dev python3-dev musl-dev postgresql-client=13+225 libpq-dev gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /opt/code/
RUN pip install -r requirements.txt
COPY ./src /opt/code/
COPY ./imgs /opt/imgs



