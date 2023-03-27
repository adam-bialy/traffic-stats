FROM  python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code

RUN apt-get update && \
    pip install -r requirements.txt

COPY . /code
