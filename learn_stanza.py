#!/usr/bin/env python
# -*- coding: utf-8 -*-
import stanza

if __name__ == '__main__':
    # https://github.com/stanfordnlp/stanza/blob/master/demo/Stanza_Beginners_Guide.ipynb
    # Note that you can use verbose=False to turn off all printed messages
    print("Downloading Chinese model...")
    stanza.download('zh', verbose=True, resources_url='stanford')

    # Build a Chinese pipeline, with customized processor list and no logging,
    # and force it to use CPU
    print("Building a Chinese pipeline...")
    zh_nlp = stanza.Pipeline('zh', processors='tokenize,lemma,pos,depparse',
                             verbose=True, use_gpu=False)
