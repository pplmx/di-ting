#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyhanlp import *

analyzer = PerceptronLexicalAnalyzer(
    'C:/Users/purpl/.virtualenvs/BuildRoleRelationship4Novel/Lib/site-packages/pyhanlp/static/data/model/perceptron/large/cws.bin',
    HanLP.Config.PerceptronPOSModelPath,
    HanLP.Config.PerceptronNERModelPath)
tokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")


def prepare(file):
    with open(file, encoding='UTF-8') as f:
        for line in f.readlines():
            if not line.strip():
                continue
            print(tokenizer.analyze(line).translateLabels())


if __name__ == '__main__':
    # prepare('惟我独仙.txt')
    print(tokenizer.analyze('冥英王楞楞的道：“他，他真的放过了你。  ”'))
