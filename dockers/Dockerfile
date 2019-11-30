FROM python:3.5.9
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \ 
    apt-get upgrade -y
RUN pip install --upgrade pip &&\
    pip install Django &&\
    pip install djangorestframework &&\
COPY ./source /source
WORKDIR /source 