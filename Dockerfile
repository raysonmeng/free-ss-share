FROM python:2
MAINTAINER Rayson Meng <rayson951005@gmail.com>

COPY . /home

# 安装libsodium
WORKDIR /home
RUN apt-get update
RUN apt-get install -y build-essential
RUN wget https://github.com/jedisct1/libsodium/releases/download/1.0.12/libsodium-1.0.12.tar.gz
RUN tar zxvf libsodium-1.0.12.tar.gz
WORKDIR /home/libsodium-1.0.12
RUN ./configure
RUN make -j2
RUN make install
RUN ldconfig


# 安装shadowsocks-libev
RUN sh -c 'printf "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list'
RUN apt update
RUN apt -t jessie-backports install -y shadowsocks-libev


# 配置python安装包
ENV PYTHONUNBUFFERED 1
WORKDIR /home
RUN pip install -r requirements.txt
RUN python setup.py develop --record installed_files.txt
