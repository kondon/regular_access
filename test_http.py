# -*- coding: utf-8 -*-
import requests

if __name__ == '__main__':
    query = {
        'id': 1
    }
    r = requests.get('https://test-sample-kondo.herokuapp.com/web/test_api.php', params=query)
    print r.status_code
    print r.encoding
    print r.headers
    print r.text
    print r.json()
