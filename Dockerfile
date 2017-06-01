FROM python:2
MAINTAINER Rayson Meng <rayson951005@gmail.com>

ENV PYTHONUNBUFFERED 1
COPY . /home
WORKDIR /home
RUN pip install -r requirements.txt
RUN python setup.py develop --record installed_files.txt