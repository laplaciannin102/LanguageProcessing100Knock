# coding: utf-8

'''
annn初見プレイ
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''

word = 'stressed'

reverse = ''

for chara in word:
    reverse = chara + reverse

print(reverse)