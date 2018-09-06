# coding: utf-8

'''
annn初見プレイ
05. n-gram
与えられたシーケンス（文字列やリストなど）から
n-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，
文字bi-gramを得よ．
'''

# 単語n-gram
def get_word_n_gram(n, sequence):
    poyo = []
    mugicha = sequence.split()

    if len(mugicha) >= n:

        for ii in range(0, len(mugicha) - n + 1):
            word = ''
            for jj in range(n):
                word += mugicha[ii + jj]

            poyo.append(word)

    else:
        poyo.append(mugicha)
    
    return poyo 


# 文字n-gram
def get_chara_n_gram(n, sequence):
    poyo = []

    if len(sequence) >= n:

        for ii in range(0, len(sequence) - n + 1):
            word = ''
            for jj in range(n):
                word += sequence[ii + jj]

            poyo.append(word)

    else:
        poyo.append(sequence)
    
    return poyo


hoge = 'I am an NLPer'

print(get_word_n_gram(2, hoge))
print(get_word_n_gram(3, hoge))
print(get_chara_n_gram(2, hoge))
print(get_chara_n_gram(3, hoge))

'''
['Iam', 'aman', 'anNLPer']
['Iaman', 'amanNLPer']
['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
['I a', ' am', 'am ', 'm a', ' an', 'an ', 'n N', ' NL', 'NLP', 'LPe', 'Per']
'''