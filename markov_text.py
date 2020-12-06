"""
基于Markov过程的文本生成:
markov_dict:  { 'word': [next_words.....], ..... }
很类似N-gram啊，确定不是受到NLP的启发才想到这个大作业的嘛
两阶markov_dict就是Tri-gram
我们只要一阶markov_dict
就这就这
"""

import os
import random

markov_dicts = {'': []}   # Start of Sentence
# 注意，一些在?后面的单词首字母不大写
sentence_sep = '.?!'    # 句子结束标志


def parse(text):
    """ 分析text，产生相应的dict"""
    # TODO: use re
    text = text.replace('\n', '')
    text = text.strip('"')
    text = text.strip(' ')
    text_list = text.split(' ')
    # 单词数太少了 或者不完整
    if len(text_list) <= 1 or text_list[-1][-1] not in sentence_sep:
        return

    last_word = ''
    for word in text_list:
        # 这对单词加入到markov_dict
        markov_dicts.get(last_word).append(word)
        # 如果markov_dict中不存在这个键，就创建
        if markov_dicts.get(word) is None:
            markov_dicts[word] = list()
        # 准备下一个
        if word[-1] not in sentence_sep:
            last_word = word
        else:
            last_word = ''


def generate(num_sentences=1, word_limit=20):
    """ 根据前面调用parse得到的dict，随机生成多个句子"""
    sentences = list()
    for _ in range(num_sentences):
        # word 是目前选中的单词
        word = random.choice(markov_dicts[''])
        sentence = list([word])
        # TODO: end with sentence_sep
        for _ in range(word_limit):
            if len(markov_dicts[word]) == 0:
                break
            # 随机选下一个单词
            word = random.choice(markov_dicts[word])
            sentence.append(word)
            if word[-1] in sentence_sep:
                break
        sentences.append(sentence)

    return sentences


def markov_main():
    # input_file = './beatles.txt'
    # input_file = './hamlet.txt'
    input_file = './bbcnews.txt'
    with open(input_file, 'r') as f:
        line = f.readline()
        while line:
            parse(line)
            line = f.readline()

    sentences = generate(10)
    for _, sentence in enumerate(sentences):
        # print(sentence)
        words = ''
        for _, word in enumerate(sentence):
            words += word + ' '
        print(words)


if __name__ == '__main__':
    markov_main()
