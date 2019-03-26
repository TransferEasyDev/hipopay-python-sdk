# -*- coding: utf-8 -*-
import base64
import json
import time
from urllib import quote

import requests
import rsa
from config import MERCHANT_API_VERSION, HP_HOST, MERCHANT_PRIVATE_KEY, MERCHANT_NO


class HipopayRequest(object):
    def __init__(self, api_url, params):
        self.url = HP_HOST.format(url=api_url)
        self.timestamp = str(time.time())
        self.params = params
        self.signature = self.__data_sign()
        self.headers = {
            "MerchantNO": MERCHANT_NO,
            "Version": MERCHANT_API_VERSION,
            "Timestamp": self.timestamp,
            "Signature": self.signature
        }
        if api_url == 'download_bill':
            self.headers["Version"] = '3.0'

        print self.url
        print json.dumps(self.params, ensure_ascii=False, indent=2)
        print json.dumps(self.headers, ensure_ascii=False, indent=2)

    def get(self):
        r = requests.get(self.url, params=self.params, headers=self.headers, verify=False)
        print r.content
        return r

    def post(self):
        r = requests.post(self.url, data=self.params, headers=self.headers, verify=False)
        print r.content
        return r

    def put(self):
        r = requests.put(self.url, data=self.params, headers=self.headers, verify=False)
        print r.content
        return r

    def delete(self):
        import urllib
        r = requests.delete(self.url + '?' + urllib.urlencode(self.params), headers=self.headers, verify=False)
        print r.content
        return r

    def __format_code(self, x):
        """ 处理编码问题, 兼容unicode, int和 float
        """
        if isinstance(x, unicode):
            return quote(x.encode("utf-8"), safe="")
        elif isinstance(x, (float, int)):
            return str(x)
        else:
            return quote(x, safe="")

    def __data_sign(self):
        """
        :param timestamp: 时间戳
        :param private_key: 私钥
        :return: 签名
        """
        # 按照key的拼音排序成key=value形式
        signature_str = "&".join((
            "=".join(map(self.__format_code, i)) for i in sorted(self.params.items())
        ))
        # 用 utf-8 编码
        signature_str = signature_str.encode("utf-8")
        # 将时间戳附到最后,用逗号隔开
        signature_str += "," + str(self.timestamp)
        # print signature_str
        pri_key = rsa.PrivateKey.load_pkcs1(MERCHANT_PRIVATE_KEY)

        signature = base64.b64encode(rsa.sign(signature_str, pri_key, "SHA-256"))
        return signature

