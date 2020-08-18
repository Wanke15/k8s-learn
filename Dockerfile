FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install vim -y && apt install python3 -y && apt install python3-pip -y && apt install tzdata -y
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN pip3 install --no-cache-dir Cython==0.29.19
RUN pip3 install --no-cache-dir gevent==20.5.2
RUN pip3 install --no-cache-dir gunicorn==19.4.5

RUN pip3 install --no-cache-dir Flask==1.1.1

COPY / /data/app

WORKDIR /data/app

ENTRYPOINT ./docker-entrypoint.sh
