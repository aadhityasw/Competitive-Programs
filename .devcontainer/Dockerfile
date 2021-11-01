FROM ubuntu:latest

RUN apt-get update
WORKDIR /
RUN apt-get -y upgrade

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /
RUN apt-get install -y --no-install-recommends git
WORKDIR /
RUN apt-get install -y default-jre
WORKDIR /
RUN apt-get install -y default-jdk
WORKDIR /
RUN apt-get install -y python3-pip
WORKDIR /
RUN apt-get install -y build-essential
