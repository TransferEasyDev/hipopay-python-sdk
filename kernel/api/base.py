# -*- coding: utf-8 -*-
from kernel.hipopay_request import HipopayRequest


class Base(object):
    def __init__(self, is_hk=False, is_cny=False):
        self.is_hk = is_hk
        self.is_cny = is_cny

    def if_cny(self, params):
        if self.is_cny:
            params['is_rmb'] = 'TRUE'
        return params

    def get_bill(self, params):
        request = HipopayRequest('download_bill', params)
        request.get()

    def get_payment(self, params):
        request = HipopayRequest('payment', params)
        request.get()

    def refund(self, params):
        request = HipopayRequest('payment_refund', params)
        request.post()

    def get_refund(self, params):
        request = HipopayRequest('payment_refund', params)
        request.get()
