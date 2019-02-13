# -*- coding:utf-8 -*-

HP_HOST = 'https://api.hipopay.com/{url}'
MERCHANT_API_VERSION = '1.0'
MERCHANT_NO = 'your_merchant_no'
MERCHANT_PRIVATE_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
your_praivate_key
-----END RSA PRIVATE KEY-----'''
HP_PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
hp_server_public_key
-----END PUBLIC KEY-----'''

# '''
# >>>1、您需要在境外的微信开放平台用境外的公司主体注册账号。
# >>>2、你需要在开放平台提交您的APP信息并申请APPID。(这两步可以由WiseCashier来代劳)
# >>>3、您需要把APPID提供给WiseCashier去绑定一个支付能力(这时需要确认结算币种)。
# >>>4、上面步骤都完成之后就可以通过我们的接口来实现微信的APP支付功能了。
#  '''
MERCHANT_APPID = 'your_app_id'
MERCHANT_MINI_APPID = 'your_app_id'
