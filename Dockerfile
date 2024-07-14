FROM python:3.10-alpine
LABEL maintainer="ecco272727@gmail.com"

WORKDIR /root

COPY requirments.txt /tmp/

RUN apk update && apk add \
    chromium \
    chromium-chromedriver \
    libuuid \
    pcre \
    mailcap \
    gcc \
    libc-dev \
    linux-headers \
    pcre-dev \
    curl \
    bash \
    xorg-server-xephyr \
    xvfb \
    fluxbox \
    tmux \
    x11vnc \
    st \
    xorg-server-xephyr \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirments.txt \
    && apk del \
    gcc \
    libc-dev \
    linux-headers \
    && rm -rf /tmp/*

RUN mkdir -p /var/log/app \
    && chmod 777 -R /var/log/app
    
COPY src /root

