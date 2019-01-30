# -*- coding: utf-8 -*-
from kernel.api.base import Base
from kernel.hipopay_request import HipopayRequest


class Alipay(Base):

    def __is_hk(self, params):
        if self.is_hk:
            params['hk_wallet'] = 'true'
        return params

    def app_pay(self, params):
        params = self.if_cny(params)
        request = HipopayRequest('alipay/app/payment', params)
        request.post()

    def wap_pay(self, params):
        params = self.if_cny(params)
        params = self.__is_hk(params)
        request = HipopayRequest('alipay/wap/payment', params)
        request.post()

    def consumer_scan_merchant(self, params):
        params = self.__is_hk(params)
        request = HipopayRequest('alipay/qrcode/payment', params)
        request.post()

    def merchant_scan_conumer(self, params):
        params = self.__is_hk(params)
        request = HipopayRequest('alipay/barcode/payment', params)
        request.post()

    def get_rate(self, params):
        request = HipopayRequest('alipay/rate', params)
        request.get()
