# -*- coding: utf-8 -*-
from kernel.api.alipay import Alipay

if __name__ == '__main__':

    params = {
        'out_trade_id': 'your_trade_id',        # 商户交易流水号  Y
        'amount': '100',                        # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
        'currency': 'HKD',                      # 计价币种 Y
        'product_info': 'test product',         # 商品信息 Y
        'client_ip': '0.0.0.0',                 # 客户端设备IP地址 Y
        'notify_url': 'your_notify_url',        # 异步通知地址  N
    }
    # is_hk 是否使用支付宝香港钱包，取值"TRUE"/"FALSE"，默认值为"FALSE"
    alipay = Alipay(is_hk=True)
    alipay.consumer_scan_merchant(params)

