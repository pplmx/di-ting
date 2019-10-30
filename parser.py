#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    并查集
    哈斯图
"""
from collections import Counter

import jieba
from pyhanlp import *

tokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")


def prepare(file):
    with open(file, encoding='UTF-8') as f:
        i = 0
        for line in f.readlines():
            i += 1
            # filter the empty line
            line = line.strip()
            if line:
                if i < 10:
                    print(i, line)
                    print(tokenizer.analyze(line).translateLabels())


def read_novel(file):
    with open(file, encoding='UTF-8') as f:
        return jieba.lcut(f.read())


if __name__ == '__main__':
    # prepare('惟我独仙.txt')
    # print(tokenizer.analyze('冥英王楞楞的道：“他，他真的放过了你。  ”'))
    ll = list(filter(lambda i: len(i) > 1, read_novel('惟我独仙.txt')))
    ll = Counter(ll)
    print(ll)
