# -*- coding: utf-8 -*-
from kernel.api.alipay import Alipay

if __name__ == '__main__':

    params = {
        'refund_no': 'hp_refund_no',        # 退款单号，和out_refund_id不可同时为空
        'out_refund_id': 'your_refund_id',  # 外部退款单号，和refund_no不可同时为空
    }
    alipay = Alipay()
    print alipay.get_refund(params)

