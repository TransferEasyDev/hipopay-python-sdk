# -*- coding: utf-8 -*-
from kernel.api.wechat_cn import WechatCn

if __name__ == '__main__':
    params = {
        'currency': 'HKD',                              # 币种	        是
    }
    wechat_cn = WechatCn()
    wechat_cn.get_rate(params)
