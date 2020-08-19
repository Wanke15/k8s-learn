FROM python:3.7.9-alpine

RUN pip install --no-cache-dir Flask==1.1.1

COPY / /data/app

WORKDIR /data/app

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
