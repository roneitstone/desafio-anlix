FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY dados /code/dados


