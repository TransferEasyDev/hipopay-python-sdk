# -*- coding: utf-8 -*-
import when
import random
from kernel.api.wechat_cn import WechatCn


def gen_no(prefix=''):
    no = prefix + when.format(when.now(), '%Y%m%d%H%M%S') + str(random.randint(10000, 99999))
    return no


# out_trade_id  过长
def test_long_trade_id():
    print 'X' * 200
    print '=====>out_trade_id  过长'
    out_trade_id = '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    params = {
        'out_trade_id': out_trade_id,             # 商户交易流水号 Y
        'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
        'currency': 'HKD',                           # 支付单结算币种
        'product_info': 'test',                      # 商品信息
        'client_ip': '127.0.0.1',                    # 客户端设备IP地址
        'notify_url': 'your_notify_url',             # 异步通知地址
    }
    print 'len of out_trade_id is {0}'.format(str(len(out_trade_id)))
    # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
    wechat_cn = WechatCn(is_cny=False)
    wechat_cn.consumer_scan_web(params)


# out_trade_id 最前有空格 中间有空格 最后有空格
def test_space_in_trade_id():
    out_trade_id_list = [' 201902271', '2019 02272', '201902273 ']
    for out_trade_id in out_trade_id_list:
        print 'X' * 200
        print '=====>out_trade_id 最前有空格 中间有空格 最后有空格'
        params = {
            'out_trade_id': out_trade_id,             # 商户交易流水号 Y
            'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
            'currency': 'HKD',                           # 支付单结算币种
            'product_info': 'test',                      # 商品信息
            'client_ip': '127.0.0.1',                    # 客户端设备IP地址
            'notify_url': 'your_notify_url',             # 异步通知地址
        }
        print 'out_trade_id is {0}'.format(out_trade_id)
        # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
        wechat_cn = WechatCn(is_cny=False)
        wechat_cn.consumer_scan_web(params)


# out_trade_id 包含特殊字符
def test_special_in_trade_id():
    special_list = [
        "-", "_", ".", "!", "*", "'",
        "(", ")", ",", "{", "}", "|", "\\", "^", "~", "[", "]", "`", "<", ">",
        "#", "%", '"', ";", "/", "?", ":", "@", "&", "=", "$", "+"
    ]

    for special in special_list:
        print 'X' * 200
        print '=====>out_trade_id 包含特殊字符'
        out_trade_id = '2019{special}0227'.format(special=special)
        params = {
            'out_trade_id': out_trade_id,             # 商户交易流水号 Y
            'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
            'currency': 'HKD',                           # 支付单结算币种
            'product_info': 'test',                      # 商品信息
            'client_ip': '127.0.0.1',                    # 客户端设备IP地址
            'notify_url': 'your_notify_url',             # 异步通知地址
        }
        print 'out_trade_id is {0}'.format(out_trade_id)
        # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
        wechat_cn = WechatCn(is_cny=False)
        wechat_cn.consumer_scan_web(params)


# product_info. 过长
def test_long_product_info():
    print 'X' * 200
    print '=====>product_info. 过长'
    product_info = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    params = {
        'out_trade_id': gen_no(),             # 商户交易流水号 Y
        'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
        'currency': 'HKD',                           # 支付单结算币种
        'product_info': product_info,                # 商品信息
        'client_ip': '127.0.0.1',                    # 客户端设备IP地址
        'notify_url': 'your_notify_url',             # 异步通知地址
    }
    print 'len of product_info is {0}'.format(str(len(product_info)))
    # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
    wechat_cn = WechatCn(is_cny=False)
    wechat_cn.consumer_scan_web(params)


# product_info 最前 中间 最后有空格
def test_space_in_product_info():
    product_info_list = [' test', 'te st', 'test ']
    for product_info in product_info_list:
        print 'X' * 200
        print '=====>product_info 最前 中间 最后有空格'
        params = {
            'out_trade_id': gen_no(),  # 商户交易流水号 Y
            'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
            'currency': 'HKD',                           # 支付单结算币种
            'product_info': product_info,                # 商品信息
            'client_ip': '127.0.0.1',                    # 客户端设备IP地址
            'notify_url': 'your_notify_url',             # 异步通知地址
        }
        print 'product_info is {0}'.format(product_info)
        # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
        wechat_cn = WechatCn(is_cny=False)
        wechat_cn.consumer_scan_web(params)


# product_info 包含繁体字 生僻字
def test_specil_chinese_in_product_info():
    # product_info_list = [u'魃', u'魈', u'魁', u'鬾', u'魑', u'魅', u'魍', u'魉',
    #                      u'叒', u'叕', u'焱', u'燚', u'沝', u'淼', u'㵘', u'㙓',
    #                      u'𨰻', u'茕', u'沆', u'瀣', u'踽', u'瓞', u'奉', u'臬',
    #                      u'龘', u'龘', u'袅', u'娜', u'呶', u'稂', u'莠', u'卬',
    #                      u'咄', u'嗟', u'蹀', u'躞', u'耄', u'耋', u'饕', u'餮',
    #                      u'囹', u'圄', u'蘡', u'薁', u'龃', u'龉', u'狖', u'轭',
    #                      u'鼯', u'靁', u'虺', u'孑', u'孓', u'栉', u'翕']

    product_info_list = ['魃', '魈', '魁', '鬾', '魑', '魅', '魍', '魉',
                         '叒', '叕', '焱', '燚', '沝', '淼', '㵘', '㙓',
                         '𨰻', '茕', '沆', '瀣', '踽', '瓞', '奉', '臬',
                         '龘', '龘', '袅', '娜', '呶', '稂', '莠', '卬',
                         '咄', '嗟', '蹀', '躞', '耄', '耋', '饕', '餮',
                         '囹', '圄', '蘡', '薁', '龃', '龉', '狖', '轭',
                         '鼯', '靁', '虺', '孑', '孓', '栉', '翕']
    for product_info in product_info_list:
        print 'X' * 200
        print '=====>product_info 包含繁体字 生僻字'
        params = {
            'out_trade_id': gen_no(),  # 商户交易流水号 Y
            'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
            'currency': 'HKD',                           # 支付单结算币种
            'product_info': product_info,                # 商品信息
            'client_ip': '127.0.0.1',                    # 客户端设备IP地址
            'notify_url': 'your_notify_url',             # 异步通知地址
        }
        print product_info
        # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
        wechat_cn = WechatCn(is_cny=False)
        wechat_cn.consumer_scan_web(params)


# product_info 包含全角符号如 "，"，"|"。"|"【"|"】"|"「"|"」"|"；"|"“"|"（" | "）" |"”"|"："|"？"
def test_full_width_in_product_info():
    product_info_list = ["，", "。", "【", "】", "「", "」", "；", "“", "（", "）", "”", "：", "？"]
    for product_info in product_info_list:
        print 'X' * 200
        print '=====>product_info 包含全角符号'
        params = {
            'out_trade_id': gen_no(),  # 商户交易流水号 Y
            'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
            'currency': 'HKD',                           # 支付单结算币种
            'product_info': product_info,                # 商品信息
            'client_ip': '127.0.0.1',                    # 客户端设备IP地址
            'notify_url': 'your_notify_url',             # 异步通知地址
        }
        print 'product_info is {0}'.format(product_info)
        # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
        wechat_cn = WechatCn(is_cny=False)
        wechat_cn.consumer_scan_web(params)
