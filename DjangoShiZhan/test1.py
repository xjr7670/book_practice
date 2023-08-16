# -*- coding: utf-8 -*-
import json
import sys
import uuid
import requests
import hashlib
import time
from importlib import reload

import time

reload(sys)


class YoudaoTranslator(object):

    def __init__(self):
        self.youdao_url = 'https://openapi.youdao.com/api'
        self.APP_KEY = '5ff5a86fc6c32a9f'
        self.APP_SECRET = 'FvxaXPuWGKdjrBVzC8hIGI2A6AxKbbmn'

    @staticmethod
    def encrypt(signStr):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode('utf-8'))
        return hash_algorithm.hexdigest()

    @staticmethod
    def truncate(q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

    def do_request(self, data):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        return requests.post(self.youdao_url, data=data, headers=headers)

    def do_translate(self, q):
        data = {}
        data['from'] = 'en'
        data['to'] = 'zh-CHS'
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = self.APP_KEY + self.truncate(q) + salt + curtime + self.APP_SECRET
        sign = self.encrypt(signStr)
        data['appKey'] = self.APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign
        data['vocabId'] = "您的用户词表ID"

        response = self.do_request(data)
        contentType = response.headers['Content-Type']
        if contentType == "audio/mp3":
            millis = int(round(time.time() * 1000))
            filePath = "合成的音频存储路径" + str(millis) + ".mp3"
            fo = open(filePath, 'wb')
            fo.write(response.content.decode('utf-8'))
            fo.close()
        else:
            resp = response.json()
            ret = []
            if resp['errorCode'] == '0':
                explain = resp['basic']['explains']

                if explain:
                    translation = '\n'.join(explain).replace('；', '\n')
                else:
                    translation = '.'.join(resp['translation'])
                ret.append(translation)
                for item in resp['web']:
                    ret.append(f'{item["key"]}: {".".join(item["value"])}')
                ret.append(f'us-phonetic: {resp["basic"]["us-phonetic"]}')
                print(ret)
                return '\n'.join(ret)
            else:
                return None


if __name__ == '__main__':
    word = 'system'
    translator = YoudaoTranslator()
    translator.do_translate(word)
