# -*- coding: utf-8 -*-
import sys
import os
import requests

def log_file(t):
    path = "D:\\heroku_http_access_log"
    f = open(path+"\\test.log",'a')
    t.encode('utf-8')
    f.write(t+"\n")
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
    log_file(r.text)
#    print r.json()
