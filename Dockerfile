# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /opt/code
COPY requirements.txt /opt/code/
RUN pip install -r requirements.txt
COPY ./src /opt/code/
COPY ./imgs /opt/imgs
RUN apt-get update && apt-get -y install postgresql


