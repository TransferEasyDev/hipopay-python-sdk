
![HipoPay](https://s.transfereasy.com/logo/hipopay-github.png)

# 全渠道跨境收款

* [官方网站](https://www.hipopay.com/)
* [体验中心](https://www.hipopay.com/Demo/index)
* [商务合作](https://www.hipopay.com/Home/cooperate)
* [开发文档](https://www.hipopay.com/Document/newDoc?page=index)

## 结构

```$xslt
├── config      # 配置文件
├── examples    # DEMO
├── kernel      # API
└── test        # 测试用例
```

## 示例

```
/**
 * 初始化环境
 */

$ cd hipopay-python-sdk
$ virtualenv ENV
$ source ./ENV/bin/active
$ (ENV) pip install -r requirements.txt
```

```
/**
 * 配置文件
 *
 * └── config
 *     └── __init__.py
 */

# 在 __init__.py 中控制生产和测试的配置文件开关
from config.test import *  # 沙盒环境
# from config.prod import *  # 生产环境

```

```
/**
 * 配置文件
 *
 * └── config
 *     ├── prod.py*
 *     └── test.py
 */
SECRET = ''         # 登录transfereasy后台进入设置页面查看
ACCOUNT_NO = ''     # 登录transfereasy后台进入设置页面查看
TE_HOST = 'https://stable-api.transfereasy.com/{url}'

```

```python
# -*- coding: utf-8 -*-
from kernel.api.wechat_cn import WechatCn

if __name__ == '__main__':
    params = {
        'out_trade_id': 'your_trade_id',             # 商户交易流水号 Y
        'amount': '10',                              # 支付单金额，单位为元，精度最多小数点后两位(如果是JPY和KRW，单位为分) Y
        'currency': 'HKD',                           # 支付单结算币种
        'product_info': 'test',                      # 商品信息
        'client_ip': '127.0.0.1',                    # 客户端设备IP地址
        'notify_url': 'your_notify_url',             # 异步通知地址
    }
    # is_cny 是否采用人民币(CNY)计价，取值"TRUE"/"FALSE"，默认值为"FALSE"
    wechat_cn = WechatCn(is_cny=False)
    wechat_cn.consumer_scan_web(params)

```

## 依赖

* requests==2.18.4
* rsa==3.4.2
* Flask==1.0.2
* nose==1.3.7
