# -*- coding: utf-8 -*-
from kernel.api.alipay import Alipay

if __name__ == '__main__':

    params = {
        'currency': 'HKD',   # 币种	是
    }
    alipay = Alipay()
    alipay.get_rate(params)

