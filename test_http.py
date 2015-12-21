# -*- coding: utf-8 -*-
import sys
import os
import requests
import json
import codecs

# httpリクエストを受け取って、標準出力+ファイルに出力する際に少しハマった備忘録
# 日本語を扱う場合の基本的な考えになると思う。
# バイト文字列・・・特定のエンコード方式(ex. utf-8)でエンコードされており、リテラルでは'あいう'のように表現する。
# ユニコード文字列・・・ユニコード文字列はUnicodeのコードポイントを並べたものであり、リテラルではu'あいう'のようにuをつける。
# プログラム内での処理であれば、そこまで意識する必要はないだろうが、今回のように外部から取得する場合は問題。
# ちなみにコードレベルであればユニコードに統一した方が楽。len()での取得値が違う。
# 標準出力にユニコードを出力させると、ユニコードからバイト文字列に変換されきれいに出てくるが、
# ファイル出力などすると大抵エラーが出る。理由としては標準出力以外だとPythonは適切なエンコード方式を選択できない。
# なので一般的にはユニコード文字列→バイト文字列(明示的にエンコードを指定しながら)→書き込みの流れになる。
# 例：print((u'あ' + u'いう').encode('utf-8'))
# 常にバイト文字列なのか、ユニコード文字列なのか意識しておくことが大事!!!


def log_file_text(t):
    path = "D:\\heroku_http_access_log"
# 今回はレスポンスでUTF-8で返却されているため、書き込む際にファイルをUTF-8で扱う必要がある。
    f = codecs.open(path+"\\test_text.log", "a", "utf-8")
    f.write(t+"\r\n")
    f.close()

def log_file_json(t):
    path = "D:\\heroku_http_access_log"
    f = codecs.open(path+"\\test_json.log", "a", "utf-8")
    f.write(t+"\r\n")
    f.close()

if __name__ == '__main__':
    query = {
        'id': 1
    }
    r = requests.get('https://test-sample-kondo.herokuapp.com/web/test_api.php', params=query)
    print r.status_code
    print r.encoding
    print r.headers
    print r.text
    log_file_text(r.text)
#   log_file(r.text)
#   Json全体をエンコードする際に使用する。逆のdecodeはjson.loads()
    enc = json.dumps(r.json(),ensure_ascii=False)
    log_file_json(enc)
#    print enc
