FROM --platform=$BUILDPLATFORM python:3.10

ENV PYTHONNUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP /Repliq

WORKDIR $APP
COPY . $APP

EXPOSE 8001

RUN pip install -U pip && pip install -r requirements.txt

RUN chmod +x $APP/script.sh
