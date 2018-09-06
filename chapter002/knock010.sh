#!/bin/sh

# 第2章: UNIXコマンドの基礎
# hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# カレントを移動
cd $(dirname $0)
pwd

# 戻り値
ret=0
hightemp_path="../data/hightemp.txt"

# 行数をカウント
wc -l "${hightemp_path}" | awk '{print $1}'

exit ${ret}

# + dirname ./knock010.sh
# + cd .
# + pwd
# なんたら/LanguageProcessing100Knock
# + ret=0
# + hightemp_path=./data/hightemp.txt
# + wc -l ./data/hightemp.txt
# + awk {print $1}
# 24
# + exit 0