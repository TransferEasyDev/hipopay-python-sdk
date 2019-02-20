# -*- coding: utf-8 -*-
from config import MERCHANT_NO
from kernel.api.wechat_cn import WechatCn

if __name__ == '__main__':

    params = {
        'merchant_no': MERCHANT_NO,
        'start_date': '20190101',
        'end_date': '20190120',
    }
    wechat_cn = WechatCn()
    wechat_cn.get_bill(params)
