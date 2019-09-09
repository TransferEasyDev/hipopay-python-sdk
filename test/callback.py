# -*- coding: utf-8 -*-

import requests


def notify():
    # url = 'http://127.0.0.1:8087/notify_url'
    url = 'http://127.0.0.1:8086/notify'
    data = {
        "status": "PAID",
        "trade_type": "NATIVE",
        "pay_amount": "0.89",
        "out_trade_id": "20190815002",
        "currency": "HKD",
        "settle_currency": "HKD",
        "pay_currency": "CNY",
        "exchange_rate": "1.0000000000",
        "finish_time": "2019-08-15 17:20:45",
        "amount": "1.00",
        "payment_no": "2019081517201983250411444",
        "trade_time": "2019-08-15 17:20:20"
    }

    headers = {
        "Timestamp": "1565861695",
        "Signature": "BKMSFfYvoLt+sy5ZIWw0zr4nf6ZAOPOD09qEP4HaIA/Rdl8G7E25YAha5D487sippyuwEfEUNRquUr9hAM0YuPd/JsLsK45LUwPv4IMn2oxXSs4ovJtFX3taw2FpitD96svjl/H4SoAN59II/yeLnl5tiisQSlPr6864Rby4iisABY1FwsEOTb7pafE04YU71fnJWBs4BLi2NBiO5B1diHbbuda+rCPd6vwbKBgAF/yFrii+lhWV7uWpAdMPp5/NLdjDvoZiqJk+3Xq0Xish6TjvrXEKqnmDPHNXebt5crhKVHss2WdRBzvS132kxTZco+cmwzqVfKp4qXoroYzi2A=="
    }
    r = requests.post(url, data, timeout=(2, 3), headers=headers)
    print r.content


if __name__ == '__main__':
    notify()
