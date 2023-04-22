#!/usr/bin/env python
# -*- coding: utf-8 -*-
import stanza

if __name__ == '__main__':
    # https://github.com/stanfordnlp/stanza/blob/master/demo/Stanza_Beginners_Guide.ipynb
    # Note that you can use verbose=False to turn off all printed messages
    # print("Downloading Chinese model...")
    # stanza.download('zh', verbose=True, resources_url='stanford')

    # Build a Chinese pipeline
    config = {
        # Comma-separated list of processors to use
        'processors': 'tokenize,lemma,pos,depparse,ner,sentiment',
        # Language code for the language to build the Pipeline in
        'lang': 'zh-hans',
        'use_gpu': False,
        'verbose': False
    }
    print("Building a Chinese pipeline...")
    zh_nlp = stanza.Pipeline(**config)
    zh_doc = zh_nlp('冥英王楞楞的道：“他，他真的放过了你。”')
    for sent in zh_doc.sentences:
        print(sent.words)
