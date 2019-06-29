from random import randint


# DECORATOR IMPLEMENTATION
def replace_char(sentence, distribution, ratio=0.1, safe_checker=None):
    len_sentence = len(sentence)
    num_operation = int(len_sentence*ratio)
    for i in range(num_operation):
        # LOOKS TOO SLOW
        pos = randint(0, len_sentence-1)
        sentence = sentence[:pos-1] + distribution.get_one() + sentence[pos:]
    return sentence

def insert_char(sentence, distribution, ratio=0.1, safe_checker=None):
    len_sentence = len(sentence)
    num_operation = int(len_sentence*ratio)
    for i in range(num_operation):
        # LOOKS TOO SLOW
        pos = randint(0, len_sentence-1)
        sentence = sentence[:pos] + distribution.get_one() + sentence[pos:]
    return sentence

def omit_char(sentence, ratio=0.1, safe_checker=None):
    len_sentence = len(sentence)
    num_operation = int(len_sentence*ratio)
    for i in range(num_operation):
        # LOOKS TOO SLOW
        pos = randint(0, len_sentence-1)
        sentence = sentence[:pos-1] + sentence[pos:]
    return sentence

def swap_char(sentence, ratio=0.1, safe_checker=None):
    len_sentence = len(sentence)
    num_operation = int(len_sentence*ratio)
    for i in range(num_operation):
        # LOOKS TOO SLOW
        pos_1 = randint(0, len_sentence-1)
        pos_2 = randint(0, len_sentence-1)
        # sentence = sentence[:pos_1] + sentence[pos:]
    return sentence