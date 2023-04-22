#!/usr/bin/env python
# -*- coding: utf-8 -*-
import stanza

from src import labels_map

if __name__ == '__main__':
    # https://github.com/stanfordnlp/stanza/blob/main/demo/Stanza_Beginners_Guide.ipynb
    # Note that you can use verbose=False to turn off all printed messages
    # print("Downloading English model...")
    # stanza.download('en')
    # print("Downloading Chinese model...")
    # stanza.download('zh', verbose=True, resources_url='stanford')

    # Build a Chinese pipeline
    config = {
        'name': 'zh',
        # Comma-separated list of processors to use
        'processors': 'tokenize,lemma,pos,depparse,ner,sentiment',
        # Language code for the language to build the Pipeline in
        'lang': 'zh',
        'use_gpu': False,
        'verbose': False
    }
    print("Building a Chinese pipeline...")
    zh_nlp = stanza.Pipeline(**config)
    zh_doc = zh_nlp('冥英王楞楞的道：“他，他真的放过了你。”')
    for i, sent in enumerate(zh_doc.sentences):
        print("[Sentence {}]".format(i + 1))
        for word in sent.words:
            # Map all work.pos to Chinese
            work_pos = labels_map.mapping(word.pos)
            print("{:12s}\t{:12s}\t{:12s}\t{:d}\t{:12s}"
                  .format(word.text, word.lemma, work_pos, word.head, word.deprel))
        print("")
