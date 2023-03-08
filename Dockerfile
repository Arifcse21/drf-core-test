FROM --platform=$BUILDPLATFORM python:3.10

ENV PYTHONNUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /repliq
COPY . /repliq

EXPOSE 8001

RUN pip install -U pip && pip install -r requirements.txt

RUN chmod +x /repliq/script.sh
