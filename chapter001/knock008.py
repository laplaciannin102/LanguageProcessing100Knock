# coding: utf-8

'''
annn初見プレイ
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''

# サイファー
def cipher(hoge):
    poyo = ''

    for chara in hoge:

        # charaが英文字でかつ小文字の時
        if (chara.isalpha()) and (chara.islower()):
            chara = chr(219 - ord(chara))
        
        poyo += chara

    return poyo

huga = 'moFFy12345aNnn'

print('huga:')
print(huga)
print('cipher(huga):')
print(cipher(huga))
print('cipher(cipher(huga)):')
print(cipher(cipher(huga)))

'''
huga:
moFFy12345aNnn
cipher(huga):
nlFFb12345zNmm
cipher(cipher(huga)):
moFFy12345aNnn
'''