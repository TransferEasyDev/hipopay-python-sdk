# -*- coding: utf-8 -*-
from kernel.api.base import Base
from kernel.hipopay_request import HipopayRequest


class WechatHk(Base):

    def app_pay(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/hk/app/payment', params)
        request.post()

    def mini_program_pay(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/hk/mini_program/payment', params)
        request.post()
