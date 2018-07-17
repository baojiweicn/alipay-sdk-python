#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditCreditriskConsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditCreditriskConsultQueryResponse, self).__init__()
        self._available_amt = None
        self._consult_result_code = None
        self._consult_result_msg = None

    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        self._available_amt = value
    @property
    def consult_result_code(self):
        return self._consult_result_code

    @consult_result_code.setter
    def consult_result_code(self, value):
        self._consult_result_code = value
    @property
    def consult_result_msg(self):
        return self._consult_result_msg

    @consult_result_msg.setter
    def consult_result_msg(self, value):
        self._consult_result_msg = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditCreditriskConsultQueryResponse, self).parse_response_content(response_content)
        if 'available_amt' in response:
            self.available_amt = response['available_amt']
        if 'consult_result_code' in response:
            self.consult_result_code = response['consult_result_code']
        if 'consult_result_msg' in response:
            self.consult_result_msg = response['consult_result_msg']
