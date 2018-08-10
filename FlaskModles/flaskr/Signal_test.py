# -*- coding:utf-8 -*-
'''
signal测试
'''
from blinker import signal

s = signal('test start')

@s.connect
def each(round):
    print('each {}'.format(round))

@s.connect
def round_two(round):
    print('round {}'.format(round))

s.connect(each)
s.connect(round_two, sender=2)
for index in range(1,4):
    s.send(index)
