# -*- coding: utf-8 -*-
from config import MERCHANT_MINI_APPID, MERCHANT_NO
from kernel.api.wechat_hk import WechatHk

if __name__ == '__main__':
    ''' 第一步 获取用户登录凭证 '''
    ''' 第二步 获取openid '''
    ''' 第三步 下单,调用下列接口,传入参数 '''
    params = {
        'merchant_no': MERCHANT_NO,                # 商户号 Y
        'out_trade_id': 'your_trande_id',          # 商户交易流水号 Y
        'amount': '1',                             # 支付单金额 Y
        'currency': 'HKD',                         # 支付单结算币种 Y 只能为HKD
        'product_info': 'test product',            # 商品信息
        'appid': MERCHANT_MINI_APPID,              # 微信appid
        'openid': 'user_openid',                   # 用户openid
        'client_ip': 'your_client_ip',             # 客户端设备IP地址
        'notify_url': 'your_notify_url',           # 异步通知地址
    }
    # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
    wechat_hk = WechatHk()
    wechat_hk.mini_program_pay(params)
