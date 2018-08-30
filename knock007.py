# coding: utf-8

'''
annn初見プレイ
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
'''

# テンプレートによる文生成
def make_sentence_from_template(x, y, z):
    poyo = str(x) + '時の' + str(y) + 'は' + str(z)
    return poyo

x = 12
y = '気温'
z = 22.4

print(make_sentence_from_template(x, y ,z))

'''
12時の気温は22.4
'''