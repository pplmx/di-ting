#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    并查集
    哈斯图
"""
from collections import Counter

import jieba
import jieba.posseg
from pyhanlp import *

tokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
crf_seg = HanLP.newSegment('crf')


def read_novel_hanlp(file):
    all_part_speech_list = []
    role_list = []
    with open(file, encoding='UTF-8') as f:
        i = 0
        for line in f:
            i += 1
            # filter the empty line
            line = line.strip()
            line = line.replace(' ', '')
            if line:
                # transfer to python string
                # line_part_speech_list = crf_seg.seg(line).__str__()
                line_part_speech_list = tokenizer.analyze(line).translateLabels().__str__().split(' ')
                # convert to tuple list
                line_part_speech_list = [(j.split('/')[0], j.split('/')[1]) for j in line_part_speech_list]
                # filter the word whose length is less than 2
                line_part_speech_list = list(filter(lambda x: len(x[0]) > 1, line_part_speech_list))
                role_list += list(filter(lambda x: x[1] == '人名', line_part_speech_list))
                all_part_speech_list += line_part_speech_list
        return all_part_speech_list, role_list


def read_novel_jieba(file):
    all_part_speech_list = []
    with open(file, encoding='UTF-8') as f:
        i = 0
        for line in f:
            i += 1
            # filter the empty line
            line = line.strip()
            if line:
                line_part_speech_list = jieba.posseg.lcut(line)
                # filter the word whose length is less than 2
                line_part_speech_list = list(filter(lambda x: len(x.word) > 1, line_part_speech_list))
                all_part_speech_list += line_part_speech_list
    return all_part_speech_list


if __name__ == '__main__':
    all_list, roles = read_novel_hanlp('惟我独仙.txt')
    # print(tokenizer.analyze('冥英王楞楞的道：“他，他真的放过了你。  ”'))
    # ll = read_novel_jieba('惟我独仙.txt')
    roles = Counter(roles)
    print(roles)
