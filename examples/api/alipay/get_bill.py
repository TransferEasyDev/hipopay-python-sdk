# -*- coding: utf-8 -*-
from config import MERCHANT_NO
from kernel.api.alipay import Alipay

if __name__ == '__main__':

    params = {
        'merchant_no': MERCHANT_NO,
        'start_date': '20190101',
        'end_date': '20190120',
    }
    alipay = Alipay()
    alipay.get_bill(params)
