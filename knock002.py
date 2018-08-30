# coding: utf-8

'''
annn初見プレイ
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して
文字列「パタトクカシーー」を得よ．
'''

pato = 'パトカー'
taku = 'タクシー'
hoge = ''

for ii in [0,1,2,3]:
    hoge = hoge + pato[ii] + taku[ii]

print(hoge)