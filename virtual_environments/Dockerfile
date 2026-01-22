FROM python:3-slim
LABEL maintainer='Jefferson Campos'
ENV PYTHONUNBUFFERED 1

ARG SECRET_KEY_ARG
ARG ALLOWED_HOSTS_ARG
ARG DEBUG_ARG
ARG REQUIREMENTS_ARG=requirements.txt

ENV SECRET_KEY=${SECRET_KEY_ARG}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS_ARG}
ENV DEBUG+${DEBUG_ARG}

COPY ./requirements.txt /requirements.txt
COPY ./requirements-dev.txt /requirements-dev.txt

RUN apt update && apt install -y libjpeg-dev zlib1g-dev python3-dev build-essential
RUN mkdir /src
WORKDIR /src

RUN useradd -ms /bin/bash alura
RUN chown -R alura:alura /src && chomod -R 775 /src/
USER alura

RUN pip install pip --upgrade && pip install -r ${REQUIREMENTS_ARG}
