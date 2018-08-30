# coding: utf-8
import knock005 as kn5

'''
annn初見プレイ
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

hogeX = 'paraparaparadise'
hogeY = 'paragraph'

X = kn5.get_chara_n_gram(2, hogeX)
Y = kn5.get_chara_n_gram(2, hogeY)
print(X)
print(Y)

# 和集合
unionXY = set(X).union(set(Y))
# 積集合
intersectionXY = set(X).intersection(set(Y))
# 差集合
differenceXY = set(X).difference(set(Y))

print('和集合：' + str(unionXY))
print('積集合：' + str(intersectionXY))
print('差集合：' + str(differenceXY))

if 'se' in set(X):
    print('Xにseは含まれています')
else:
    print('Xにseは含まれていません')

if 'se' in set(Y):
    print('Yにseは含まれています')
else:
    print('Yにseは含まれていません')

'''
和集合：{'ad', 'ra', 'ag', 'pa', 'is', 'ar', 'ph', 'gr', 'ap', 'di', 'se'}
積集合：{'pa', 'ar', 'ra', 'ap'}
差集合：{'ad', 'se', 'is', 'di'}
Xにseは含まれています
Yにseは含まれていません
'''