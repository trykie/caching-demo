FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=utf-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
        postgresql-client && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/requirements.txt
RUN mkdir /project
COPY ./project /project
WORKDIR /project

ARG DEV=false
RUN python -m venv /py-venv &&  \
    /py-venv/bin/pip install --upgrade pip && \
    /py-venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

RUN useradd --create-home django-user
ENV PATH="/py-venv/bin:$PATH"
USER django-user
