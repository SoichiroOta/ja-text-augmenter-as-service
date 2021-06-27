FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY . /opt/api
WORKDIR /opt/api
RUN pip3 install -r requirements.txt
