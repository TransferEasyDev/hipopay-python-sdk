# -*- coding: utf-8 -*-
from kernel.api.base import Base
from kernel.hipopay_request import HipopayRequest


class WechatCn(Base):

    def app_pay(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/app/payment', params)
        request.post()

    def mp_pay(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/mp/payment', params)
        request.post()

    def mini_program_pay(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/mini_program/payment', params)
        request.post()

    def consumer_scan_web(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/web/payment', params)
        request.post()

    def consumer_scan_device(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/qrcode/payment', params)
        request.post()

    def merchant_scan_consumer(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('wechatpay/barcode/payment', params)
        request.post()

    def get_rate(self, params):
        request = HipopayRequest('wechatpay/rate', params)
        request.get()
