# syntax=docker/dockerfile:1

FROM python:3.9-buster
LABEL Maintainer="Ali Raza Zaidi"

COPY . /app
WORKDIR /app
USER root

RUN apt update
RUN pip install -r requirements.txt

CMD ["python3", "tweet.py"]