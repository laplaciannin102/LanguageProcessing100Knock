# coding: utf-8
import random

'''
annn初見プレイ
09. Typoglycemia
スペースで区切られた単語列に対して，
各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに
並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
を与え，その実行結果を確認せよ．
'''

# タイポグリセミア
# Typoglycemiaとは、単語を構成する文字を並べ替えても、
# 最初と最後の文字が合っていれば読めてしまう現象のことである。
def typoglycemia(hoge):
    # 戻り値poyo
    poyo = ''

    for word in hoge.split():
        if len(word) <= 4:
            poyo += ' ' + word
            continue
        
        mid_word = word[1:-1]
        mid_list = list(mid_word)
        # 真ん中だけシャッフル
        # 文字列のままだとシャッフルできないらしい(´・ω・｀)
        random.shuffle(mid_list)
        mid_shuffle = ''
        for x in mid_list:
            mid_shuffle += x

        arranged_word = word[0] + mid_shuffle + word[-1]
        poyo += ' ' + arranged_word
    
    poyo = poyo[1:]

    return poyo

example = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print('元:')
print(example)
print('Typoglycemia:')
print(typoglycemia(example))

'''
元:
I couldn't believe that I could actually understand what I was reading : the phenomenal power
of the human mind .
Typoglycemia:
I cnu'odlt bvieele that I cuold alalcuty unerstadnd what I was ridaneg : the pnhnmaeeol pweor
of the huamn mind .
'''