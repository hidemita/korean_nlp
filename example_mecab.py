# -*- coding: utf-8 -*-

import MeCab

tagger=MeCab.Tagger()
parse = tagger.parse(u'저는 내일 친구하고 영화를 봅니다.')
print(parse)

for l in parse.splitlines():
    result = l.rstrip().split()
    if len(result) != 2:
        continue
    elem = result[0]
    data = result[1].split(',')
    print(f'{elem}:{data}')
