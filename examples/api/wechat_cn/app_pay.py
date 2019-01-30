# -*- coding: utf-8 -*-
from config import MERCHANT_APPID
from kernel.api.wechat_cn import WechatCn

if __name__ == '__main__':
    ''' 第一步 / 请求预支付接口 '''
    params = {
        'out_trade_id': 'your_trade_id',              # 商户交易流水号 Y
        'amount': '1',                                # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
        'currency': 'HKD',                            # 结算币种 Y
        'product_info': 'test product',               # 商品信息 Y
        'appid': MERCHANT_APPID,                      # 微信开放平台分配的appid	Y
        'client_ip': 'test_agent_order_id',           # 客户端设备IP地址 Y
        'notify_url': 'test_product_id',              # 异步通知地址 N
    }
    # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
    wechat_cn = WechatCn(is_cny=False)
    wechat_cn.app_pay(params)

    ''' 第二步 / 调用微信支付SDK '''
    ''' 第三步 / 获取订单状态 '''