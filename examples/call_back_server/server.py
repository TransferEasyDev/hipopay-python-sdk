# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

from kernel.callback_sign import verify_hp_signature

app = Flask(__name__)
app_host = '0.0.0.0'
app_port = 8086

'''
status	        Y	INIT: 等待付款;PAID: 支付成功;FAIL: 支付失败; EXPIRED: 订单失效;
openid	        N	支付渠道为微信支付时返回
trade_type	    Y	交易类型
exchange_rate	Y	汇率(一个外币 = 多少个人民币)
payment_no	    Y	支付单号
currency	    Y	支付单币种，详见货币编码
amount	        Y	支付单金额
trade_time	    Y	交易时间
pay_currency	Y	支付币种，详见货币编码
pay_amount	    Y	支付金额
out_trade_id	Y	商户交易流水号
'''


@app.route('/notify_url', methods=['GET', 'POST'])
@verify_hp_signature
def notify_url(**kwargs):
    import json
    params = dict(
        status=request.values.get('status'),
        openid=request.values.get('openid'),
        trade_type=request.values.get('trade_type'),
        exchange_rate=request.values.get('exchange_rate'),
        payment_no=request.values.get('no'),
        currency=request.values.get('currency'),
        amount=request.values.get('amount'),
        trade_time=request.values.get('trade_time'),
        pay_currency=request.values.get('pay_currency'),
        pay_amount=request.values.get('pay_amount'),
        out_trade_id=request.values.get('agent_order_id'),
    )
    print json.dumps(params, ensure_ascii=False, indent=2)
    d = {'meta': {
        'success': True, 'status_code': 200,
        'message': "Requset Successes"
    }}
    return jsonify(d)


