FROM python:3

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
RUN apt-get update && apt-get install -y g++ default-jdk git vim
RUN pip install konlpy

# install MeCab-korean adaptation
WORKDIR /root
ADD https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh /tmp
RUN /bin/bash /tmp/mecab.sh

# bottle http server
RUN pip install flask
ADD service/ /root/service

EXPOSE 8080
