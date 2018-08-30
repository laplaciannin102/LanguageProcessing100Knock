'''
annn初見プレイ
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''

hoge = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
huga = []
huga = list(hoge.split())

poyo = []

for word in huga:
    word = word.replace(',', '')
    word = word.replace('.', '')
    print(word)
    poyo.append(len(word))

print(poyo)

'''
Now
I
need
a
drink
alcoholic
of
course
after
the
heavy
lectures
involving
quantum
mechanics
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
'''