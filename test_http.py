# -*- coding: utf-8 -*-
import sys
import os
import requests
import json
import codecs
from datetime import datetime
import random
import time

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


def log_file_text(st_code,t = "index.api"):
    path = "D:\\heroku_http_access_log"
# 今回はレスポンスでUTF-8で返却されているため、書き込む際にファイルをUTF-8で扱う必要がある。
    now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if st_code == "0":
        f = open(path+"\\test_index.log", "a")
        f.write(now_time+" :"+t+"\r\n")
        f.close()
    else:
        f = codecs.open(path+"\\test_index.log", "a", "utf-8")
        f.write(now_time+" :code"+st_code+" :"+t+"\r\n")
        f.close()

def log_file_json(st_code,t):
    path = "D:\\heroku_http_access_log"
    now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if st_code == "0":
        f = open(path+"\\test_api.log", "a")
        f.write(now_time+" :"+t+"\r\n")
        f.close()
    else:
        f = codecs.open(path+"\\test_api.log", "a", "utf-8")
        f.write(now_time+" :code"+st_code+" :"+t+"\r\n")
        f.close()

def log_file_error(error_m):
    path = "D:\\heroku_http_access_log"
# 今回はレスポンスでUTF-8で返却されているため、書き込む際にファイルをUTF-8で扱う必要がある。
    f = open(path+"\\error.log", "a")
    now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    f.write(now_time+" :"+error_m+"\r\n")
    f.close()

def randam_create():
    #access_n = random.randint(1, 10)
    access_n = 3
    #select_f = random.randint(0,1)
    select_f = 0
    select_i = random.randint(0,100)
    return (access_n,select_f,select_i)

if __name__ == '__main__':
    access_num,select_flag, select_id= randam_create()

    print access_num
    print select_flag

    for i in range(access_num):
        time.sleep(2.0)

        if select_flag == 0:
            access_URL = 'https://test-sample-kondo.herokuapp.com/web/test_api.php'
            query = {
                'id': select_id
            }
            try:
                log_file_json("0","------------通信開始-------------")
                r = requests.get(access_URL, params=query)
                print r.status_code
                print r.encoding
                print r.headers
    #           Json全体をエンコードする際に使用する。逆のdecodeはjson.loads()
                enc = json.dumps(r.json(),ensure_ascii=False)
                log_file_json(str(r.status_code),enc)
    #           print enc
            except Exception as e:
                log_file_error(str(type(e)))
                break
            finally:
                log_file_json("0","------------通信終了-------------")


        else:
            access_URL = 'https://test-sample-kondo.herokuapp.com/web/index.php'

            try:
                log_file_text("0","------------通信開始-------------")
                r = requests.get(access_URL)
                print r.status_code
                print r.encoding
                print r.headers
    #           print r.text
                log_file_text(str(r.status_code))
    #           log_file(r.text)
            except Exception as e:
                log_file_error(str(type(e)))
                break
            finally:
                log_file_text("0","------------通信終了-------------")
