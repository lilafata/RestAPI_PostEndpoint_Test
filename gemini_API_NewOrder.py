###############################################################################################
#
# DATE:         12/30/2019
# AUTHOR:       Lila Fata
# FILE:         gemini_API_NewOrder.py
# DESCRIPTION:  This file contains the class and methods to test the RESP API endpoint for
#               Post request 'New Order' using Gemini sandbox.
#
# NOTES:        Here are assumptions/instructions -
#               1) This program was executed with IDLE Python 3.7 on windows 10
#               2) Pytest is used to test the REST API endpoint for Post 'New Order'
#               3) Could have used parameterized testing, to reduce number of test functions
#                    * will do this on my own
#               4) Other tools were considered, such as Django, but decided on Pytest
#                    * will improve on automation test tool, if opportunity exists
#               5) Refer to the test_gemini_API_NewOrder.py file on running test cases
#
# REFERENCE:    Here's link to documentation on Gemini REST API New Order -
#               *  https://docs.gemini.com/rest-api/#new-order
#
###############################################################################################

import pytest
import requests
import json
import base64
import hmac
import hashlib
import datetime, time

#
# Definitions for NewOrder parameters:
#   *  My Key and Secret codes to Gemini sandbox for testing purposes
#   *  Gemini sandbox URL
#   *  endpoint to NewOrder
#
myKey = 'account-t5rzQ6wSoEZ6GuOJJaS8'
mySecret = 'g9yjAAwiE9ABFmLiz7CLgngqypD'
baseURL = "https://api.sandbox.gemini.com"
endPoint = "/v1/order/new"
        
#
# The class 'gemini_PostAPI_NewOrder' contain the initialization and test methods to
# perform following:
#   *  Takes in the data from a test function
#   *  Populates the New Order payload structure
#   *  Creates request header
#   *  Post the New Order request
#
class gemini_PostAPI_NewOrder:

        def __init__(self, newOrderParameters):
                self.base_url = baseURL
                self.endpoint = endPoint
                self.url = self.base_url + self.endpoint
                self.gemini_api_key = myKey
                self.gemini_api_secret = mySecret.encode()
                self.t = datetime.datetime.now()
                self.payload_nonce = str(int(time.mktime(self.t.timetuple())*1000))
                self.payload = {
                        "request": self.endpoint,
                        "nonce": self.payload_nonce,
                        "symbol": newOrderParameters['symbol'],
                        "amount": newOrderParameters['amount'],
                        "price": newOrderParameters['price'],
                        "side": newOrderParameters['side'],
                        "type": newOrderParameters['type']
                }

        def newOrder_RequestHeader(self):
                self.encoded_payload = json.dumps(self.payload).encode()
                self.b64 = base64.b64encode(self.encoded_payload)
                self.signature = hmac.new(self.gemini_api_secret, self.b64, hashlib.sha384).hexdigest()
                self.request_headers = {
                        'Content-Type': "text/plain",
                        'Content-Length': "0",
                        'X-GEMINI-APIKEY': self.gemini_api_key,
                        'X-GEMINI-PAYLOAD': self.b64,
                        'X-GEMINI-SIGNATURE': self.signature,
                        'Cache-Control': "no-cache"
                }

        def newOrder_Post(self):
                self.newOrder_RequestHeader()
                response = requests.post(url=self.url, data=None, headers=self.request_headers)
                new_order = response.json()
                return new_order, response

        def newOrder_Post_InvalidEndpoint(self):
                self.payload['request'] = "/v1/order/newInvalid"
                self.newOrder_RequestHeader()
                response = requests.post(url=self.url, data=None, headers=self.request_headers)
                new_order = response.json()
                return new_order, response        

        def newOrder_Post_InvalidBaseURL(self):
                invalidURL = "https://api.sandbox.geminiInvalid.com"
                assert baseURL != invalidURL
                new_order = "NULL"
                response = "Invalid base URL"
                return new_order, response

#
# The class 'gemini_PostAPI_NewOrder_OptionParms' contain the initialization and test methods with
# all optional parameters (client_order_id, min_amount, options, stop_price) to perform following:
#   *  Takes in the data, including optional parameters, from a test function
#   *  Populates the New Order payload structure, including optional parameters
#   *  Creates request header
#   *  Post the New Order request
#
class gemini_PostAPI_NewOrder_OptionParms:

        def __init__(self, newOrderParameters):
                self.base_url = baseURL
                self.endpoint = endPoint
                self.url = self.base_url + self.endpoint
                self.gemini_api_key = myKey
                self.gemini_api_secret = mySecret.encode()
                self.t = datetime.datetime.now()
                self.payload_nonce = str(int(time.mktime(self.t.timetuple())*1000))
                self.payload = {
                        "request": self.endpoint,
                        "nonce": self.payload_nonce,
                        "client_order_id": newOrderParameters['client_order_id'],
                        "symbol": newOrderParameters['symbol'],
                        "amount": newOrderParameters['amount'],
                        "min_amount": newOrderParameters['min_amount'],
                        "price": newOrderParameters['price'],
                        "side": newOrderParameters['side'],
                        "type": newOrderParameters['type'],
                        "options": newOrderParameters['options'],
                        "stop_price": newOrderParameters['stop_price'],
                }

        def newOrder_RequestHeader(self):
                self.encoded_payload = json.dumps(self.payload).encode()
                self.b64 = base64.b64encode(self.encoded_payload)
                self.signature = hmac.new(self.gemini_api_secret, self.b64, hashlib.sha384).hexdigest()
                self.request_headers = {
                        'Content-Type': "text/plain",
                        'Content-Length': "0",
                        'X-GEMINI-APIKEY': self.gemini_api_key,
                        'X-GEMINI-PAYLOAD': self.b64,
                        'X-GEMINI-SIGNATURE': self.signature,
                        'Cache-Control': "no-cache"
                }

        def newOrder_optionParms(self):
                self.newOrder_RequestHeader()
                response = requests.post(url=self.url, data=None, headers=self.request_headers)
                new_order = response.json()
                return new_order, response



        
