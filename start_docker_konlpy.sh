#!/bin/bash

docker run --rm -d -it -p 8080:8080 --name konlpy konlpy
docker cp ./example_mecab.py konlpy:/root/
docker cp ./example_okt.py konlpy:/root/

docker exec -it -d konlpy python service/server.py
