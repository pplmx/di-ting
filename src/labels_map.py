# Universal POS
POS_MAP = {
    'ADJ': '形容词',
    'ADP': '介词',
    'ADV': '副词',
    'AUX': '助动词',
    'CCONJ': '并列连词',
    'DET': '限定词',
    'INTJ': '感叹词',
    'NOUN': '名词',
    'NUM': '数词',
    'PART': '助词',
    'PRON': '代词',
    'PROPN': '专有名词',
    'PUNCT': '标点符号',
    'SCONJ': '从属连词',
    'SYM': '符号',
    'VERB': '动词',
    'X': '其他'
}

# Named Entity Types
NER_MAP = {
    'PERSON': '人名',
    'NORP': '民族或宗教团体',
    'FAC': '设施',
    'ORG': '组织',
    'GPE': '地理政治实体',
    'LOC': '地点',
    'PRODUCT': '产品',
    'EVENT': '事件',
    'WORK_OF_ART': '艺术作品',
    'LAW': '法律',
    'LANGUAGE': '语言',
    'DATE': '日期',
    'TIME': '时间',
    'PERCENT': '百分比',
    'MONEY': '货币',
    'QUANTITY': '数量',
    'ORDINAL': '序数词',
    'CARDINAL': '基数词'
}

# Dependency Relations
DEP_MAP = {
    'ACL': '从属限定词',
    'ADVCL': '副词性从句',
    'ADVMOD': '副词修饰语',
    'AMOD': '形容词修饰语',
    'APPOS': '同位语',
    'AUX': '助动词',
    'CASE': '格位',
    'CC': '并列连词',
    'CCOMP': '补语从句',
    'CLF': '量词',
    'COMPOUND': '复合',
    'CONJ': '并列',
    'COP': '系动词',
    'CSUBJ': '主语从句',
    'DEP': '依存关系',
    'DET': '限定词',
    'DISCOURSE': '话语元素',
    'DISLOCATED': '错位构造',
    'EXPL': '虚位成分',
    'FIXED': '固定表达式',
    'FLAT': '扁平化名称',
    'GOESWITH': '连字符构造',
}

# Morphological Features
MORPH_MAP = {
    'ABBR': '缩写',
    'ANIMACY': '生命力',
    'ASPECT': '体',
    'CASE': '格',
    'DEFINITE': '定冠词',
    'DEGREE': '程度',
    'GENDER': '性别',
    'MOOD': '语气',
    'NUMTYPE': '数词类型',
    'NUMBER': '数',
    'PERSON': '人称',
    'POLARITY': '极性',
}


def mapping(label):
    label = label.upper()
    if label in POS_MAP:
        return POS_MAP[label]
    elif label in NER_MAP:
        return NER_MAP[label]
    elif label in DEP_MAP:
        return DEP_MAP[label]
    elif label in MORPH_MAP:
        return MORPH_MAP[label]
    else:
        return label
