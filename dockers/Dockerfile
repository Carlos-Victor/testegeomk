FROM python:3.5.9
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get upgrade && \
    apt-get install tzdata
RUN pip install --upgrade pip &&\
    pip install Django &&\
    pip install djangorestframework &&\
    pip install psycopg2
COPY ./source /source
WORKDIR /source 