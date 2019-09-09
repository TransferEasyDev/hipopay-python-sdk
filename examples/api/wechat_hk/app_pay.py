# -*- coding: utf-8 -*-
from config import MERCHANT_APPID
from kernel.api.wechat_hk import WechatHk

if __name__ == '__main__':
    ''' 第一步 / 请求预支付接口 '''
    params = {
        'out_trade_id': 'your_trade_id',              # 商户交易流水号 Y
        'amount': '1',                                # 支付金额 Y
        'currency': 'HKD',                            # 结算币种 只能为HKD
        'product_info': 'test product',               # 商品信息 Y
        'appid': MERCHANT_APPID,                      # 微信开放平台分配的appid	Y
        'client_ip': 'test_agent_order_id',           # 客户端设备IP地址 Y
        'notify_url': 'test_product_id',              # 异步通知地址 N
        # 'surcharge': 'FALSE'                        # 是否收取手续费 "TRUE" / "FALSE"
    }
    wechat_hk = WechatHk()
    wechat_hk.app_pay(params)

    ''' 第二步 / 调用微信支付SDK '''  # 香港钱包预支付返回值比较少, 终端SDK正常传入即可, 其他参数值随意填写
