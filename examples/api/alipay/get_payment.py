# -*- coding: utf-8 -*-
from kernel.api.alipay import Alipay

if __name__ == '__main__':

    params = {
        'payment_no': 'hp_payment_no',        # 支付单号 N
        'out_trade_id': 'your_trade_id',      # 商户交易流水号 N
    }
    alipay = Alipay()
    alipay.get_payment(params)

