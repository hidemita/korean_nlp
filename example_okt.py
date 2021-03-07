# -*- coding: utf-8 -*-

from konlpy.tag import Okt

okt = Okt()

s = u'저는 내일 친구하고 영화를 봅니다.'

print(okt.morphs(s))
print(okt.pos(s, norm=True))
print(okt.pos(s, norm=True, stem=True))
