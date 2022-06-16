FROM python:3.9
LABEL maintainer="Astapenko Dmitry <dismyt@ya.ru>"

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY ./app /app

# Build packages
RUN pip install --upgrade pip &&  \
    pip install -r ./requirements.txt
