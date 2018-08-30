'''
annn初見プレイ
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）
への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

hoge = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
huga = hoge.split()

dict_poyo = {}

for ii in range(len(huga)):
    poyo = huga[ii]
    
    if ii+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        poyo = poyo[0]
    elif len(poyo) >= 2:
        poyo = poyo[0] + poyo[1]
    else:
        poyo = poyo[0]

    dict_poyo[str(ii+1)] = poyo

print(dict_poyo)

'''
{'1': 'H', '2': 'He', '3': 'Li', '4': 'Be', '5': 'B', '6': 'C', '7': 'N', '8': 'O', '9': 'F',
'10': 'Ne', '11': 'Na', '12': 'Mi', '13': 'Al', '14': 'Si', '15': 'P', '16': 'S', '17': 'Cl',
'18': 'Ar', '19': 'K', '20': 'Ca'}
'''