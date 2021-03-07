# Korean NLP experments

## Overview

 For learning Korean language.

## Docker

### build docker file

```shell
bash ./build_docker_konlpy.sh
```

### run docker container

```shell
bash ./start_docker_konlpy.sh
```

### example: run in the docker containter

```shell
docker exec -it konlpy bash
python example_mecab.py
python example_okt.py
```

## example: http client

- curl post example

```shell
bash test_post_by_curl.sh
```

- python post example

```shell
pip install requests
python test_post_by_python.py -t
```

```shell
pip install requests
python test_post_by_python.py -q "저는 내일 친구하고 영화를 봅니다."
```
