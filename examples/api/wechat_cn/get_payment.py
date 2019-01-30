# -*- coding: utf-8 -*-
from kernel.api.wechat_cn import WechatCn

if __name__ == '__main__':
    params = {
        'payment_no': 'hp_payment_no',        # 支付单号 N
        'out_trade_id': 'your_trade_id',      # 商户交易流水号 N
    }
    wechat_cn = WechatCn()
    wechat_cn.get_payment(params)
