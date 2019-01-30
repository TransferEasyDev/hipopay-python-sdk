# -*- coding: utf-8 -*-
import base64
from functools import wraps

import rsa
from config import HP_PUBLIC_KEY
from flask import request


def signature_verify(data, signature, timestamp):
    """
    :param data: 表单数据
    :param signature: 签名
    :param timestamp: 时间戳
    :return: 验签结果
    """
    # 按照key的拼音排序成key=value形式
    signature_str = "&".join((
        "=".join(i) for i in sorted(data.items())
    ))
    # 用 utf-8 编码
    signature_str = signature_str.encode("utf-8")
    signature_str += "," + str(timestamp)
    # base64解码签名
    signature = base64.b64decode(signature)

    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(HP_PUBLIC_KEY)
    try:
        return rsa.verify(signature_str, signature, pub_key)
    except:
        return False


def verify_hp_signature(f):
    """ 验证签名 """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature = request.headers.get('Signature')
        timestamp = request.headers.get('Timestamp')

        try:
            if not signature_verify(request.values, signature, timestamp):
                raise Exception("Signature Can't Verify")

            return f(*args, **kwargs)
        except:
            raise

    return decorated_function
