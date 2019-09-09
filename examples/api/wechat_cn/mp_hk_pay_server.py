# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import render_template

app = Flask(__name__)
app_host = '0.0.0.0'
app_port = 8086


'''为香港钱包公众号支付提供h5页面'''
'''静态资源路径原因所以放在了这里, 抱歉'''


@app.route('/hk_mp_pay', methods=['GET', 'POST'])
def hk_mpay(**kwargs):
    openid = request.values.get('openid')
    merchant_no = request.values.get('merchant_no')
    print openid
    print merchant_no
    d = {'meta': {
        'success': True, 'status_code': 200,
        'message': "Requset Successes"
    }}
    return render_template("mp_hk_pay_index.html", openid=openid, merchant_no=merchant_no)


if __name__ == '__main__':
    app.run(host=app_host, port=app_port)
