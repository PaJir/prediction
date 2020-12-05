"""
基于Markov过程的文本生成:
markov_dict:  { 'word': [next_words.....], ..... }
"""

import os
import random

markov_dicts = {'': []}   # Start of Sentence
sentence_sep = '.?!'    # 句子结束标志


def parse(text):
    """ 分析text，产生相应的dict"""
    text_list = list(text)
    for value in text_list:
        if value == ' ':
            text_list.remove(value)
    for word in text_list:
        if word not in sentence_sep:
            markov_dicts[word] = list(
                set([text_list[j+1] for j in range(len(text_list)-1) if text_list[j] == word]))

    pass


def generate(num_sentences=1, word_limit=20):
    """ 根据前面调用parse得到的dict，随机生成多个句子"""
    first_word = random.choice(list(markov_dicts.keys()))
    sentence = []
    while True:
        next_word = markov_dicts[first_word]
        sentence += next_word
        first_world = next_word
        if first_word in sentence_sep:
            return sentence
    pass


def markov_main():

    text = 'X Y Z. X Z Y? Y X Z! Z Z Z. Y Z Y.'
    parse(text)
    print(generate(4))


if __name__ == '__main__':
    markov_main()
