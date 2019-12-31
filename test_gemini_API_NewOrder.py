###############################################################################################
#
# DATE:         12/30/2019
# AUTHOR:       Lila Fata
# FILE:         test_gemini_API_NewOrder.py
# DESCRIPTION:  This file contains the Test Suite with all the test functions to test the
#               Gemini New Order classes/methods in gemini_API_NewOrder.py:
#                 * Positive test suites (eg. required parameters, optional parameters)
#                 * Negative test suites (eg. invalid parameters, nonce not increasing)
#
# NOTES:        Here are assumptions/instructions to run this script -
#               1) This test suite was executed with IDLE Python 3.7 on windows 10
#               2) The pytest command used to run the test suite is as follows:
#                    pytest -s test_gemini_API_NewOrder.py
#               3) There are a total of 41 test cases
#                    * probably could have more test cases, and will do this on my own
#               4) Could have also used assert() for validation
#                    * will do this on my own
#               5) Could have separate this one test file into multiple files
#                    * will do this on my own
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

from gemini_API_NewOrder import gemini_PostAPI_NewOrder
from gemini_API_NewOrder import gemini_PostAPI_NewOrder_OptionParms

#
# Definitions for response codes
#
HTTP_SUCCESS = 200

#
# Positive Test suite containing following test cases, with no optional parameters:
#   * test_newOrder_btcusd()
#   * test_newOrder_btcusd_amount7()
#   * test_newOrder_btcusd_price9999()
#   * test_newOrder_btcusd_sell()
#
def test_newOrder_btcusd():
        print(end='\n')
        print(end='\n') 
        print("##########  Executing Positive test suite where symbol = btcusd, with no optional parameters ##########")
        print(end='\n')        
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd()")
        print(end='\n')        
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_btcusd_price9999():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "9999.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_price9999()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_Post_amount7():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "7",
                "price": "9999.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_amount7()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS       
        print(end='\n')

def test_newOrder_btcusd_sell():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "sell",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_sell()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

#
# Negative Test suite containing following test cases, with missing required parameters:
#   * test_newOrder_btcusd_missingSymbol()
#   * test_newOrder_btcusd_missingAmount()
#   * test_newOrder_btcusd_missingPrice()
#   * test_newOrder_btcusd_missingSide()
#   * test_newOrder_btcusd_missingType()
#
def test_newOrder_btcusd_missingSymbol():
        print(end='\n')
        print(end='\n') 
        print("##########  Executing Negative test suite where required parameters are missing  ##########")
        print(end='\n')
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session        
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_missingSymbol()")
        print(end='\n')        
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')

def test_newOrder_btcusd_missingAmount():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_missingAmount()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')

def test_newOrder_btcusd_missingPrice():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_missingPrice()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')

def test_newOrder_btcusd_missingSide():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_missingSide()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')
        
def test_newOrder_btcusd_missingType():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": ""
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_missingType()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')

#
# Negative Test suite containing following test case, with invalid endpoint or baseURL:
#   * test_newOrder_btcusd_invalidEndpoint()
#   * test_newOrder_btcusd_invalidBaseURL()
#
def test_newOrder_btcusd_invalidEndpoint():
        print(end='\n')
        print(end='\n') 
        print("##########  Executing Negative test suite where endpoint/URL is invalid  ##########")
        print(end='\n')
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session        
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post_InvalidEndpoint()
        print("Test Result: test_newOrder_btcusd_invalidEndpoint()")
        print(end='\n')        
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')

def test_newOrder_btcusd_invalidBaseURL():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session        
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post_InvalidBaseURL()
        print("Test Result: test_newOrder_btcusd_invalidBaseURL()")
        print(end='\n')  
        assert gemini_NewOrder == "NULL"
        print("new order = ", gemini_NewOrder)
        print("response = ", response)        
        print(end='\n')

#
# Positive Test suite containing following test cases, with no optional parameters:
#   * test_newOrder_ethusd()
#   * test_newOrder_ethbtc()
#   * test_newOrder_zecusd()
#   * test_newOrder_zecbtc()
#   * test_newOrder_zecltc()
#   * test_newOrder_bchusd()
#   * test_newOrder_bchbtc()
#   * test_newOrder_bcheth()
#   * test_newOrder_ltcusd()
#   * test_newOrder_ltcbtc()
#   * test_newOrder_ltceth()
#
def test_newOrder_ethusd():
        print(end='\n')
        print(end='\n') 
        print("##########  Executing Positive test suite to test most other symbols, with no optional parameters ##########")
        print(end='\n')
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ethusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ethusd()")
        print(end='\n')        
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_ethbtc():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ethbtc",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ethbtc()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_zecusd():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "zecusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_zecusd()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_zecbtc():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "zecbtc",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_zecbtc()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_zecltc():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "zecltc",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_zecltc()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_bchusd():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "bchusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_bchusd()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_bchbtc():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "bchbtc",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_bchbtc()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_bcheth():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "bcheth",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_bcheth()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_ltcusd():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ltcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ltcusd()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_ltcbtc():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ltcbtc",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ltcbtc()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_ltceth():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ltceth",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ltceth()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')

def test_newOrder_ltcbch():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ltcbch",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ltcbch()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code == HTTP_SUCCESS
        print(end='\n')
        
#
# Negative Test suite containing following test cases, with no optional parameters:
#   * test_newOrder_btcusd_symbolMisspelled()
#   * test_newOrder_btcusd_amountNegative()
#   * test_newOrder_btcusd_priceNegative()
#   * test_newOrder_btcusd_sideMisspelled()
#   * test_newOrder_btcusd_typeMisspelled()
#   * test_newOrder_zecbch()
#   * test_newOrder_ltcbch()
#
def test_newOrder_btcusd_symbolMisspelled():
        print(end='\n')
        print(end='\n')
        print("##########  Executing Negative test suite, with some typos in parms and different symbols ##########")
        print("  ~~~~~~~~~~  NOTE:  Expecting 'Invalid****' reasons in the results  ~~~~~~~~~~")
        print(end='\n')        
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "bbtcusd",
                "amount": "7",
                "price": "9999.00",
                "side": "buy",
                "type": "exchangee limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_symbolMisspelled()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)
        print(end='\n')

def test_newOrder_btcusd_amountNegative():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "-5",
                "price": "3633.00",
                "side": "sell",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_amountNegative()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)        
        print(end='\n')

def test_newOrder_btcusd_priceNegative():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "-3633.00",
                "side": "sell",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_priceNegative()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)        
        print(end='\n')

def test_newOrder_btcusd_sideMisspelled():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "buyy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_sideMisspelled()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)        
        print(end='\n')
                      
def test_newOrder_btcusd_typeMisspelled():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "btcusd",
                "amount": "5",
                "price": "3633.00",
                "side": "sell",
                "type": "exchang limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_typeMisspelled()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)        
        print(end='\n')

def test_newOrder_zecbch():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "zecbch",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_zecbch()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)            
        print(end='\n')

def test_newOrder_ltcbch():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "symbol": "ltcbch",
                "amount": "5",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit"
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_ltcbch()")
        print(end='\n')
        print(gemini_NewOrder)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)    
        print(end='\n')
        
#
# Positive Test suite containing following test cases, with all the optional parameters
# (client_order_id, min_amount, options, stop_price):
#   * test_newOrder_btcusd_clientOrderId()
#   * test_newOrder_btcusd_minAmount()
#   * test_newOrder_btcusd_OptionsMakerCancel()
#   * test_newOrder_btcusd_OptionsImmediateCancel()
#   * test_newOrder_btcusd_OptionsFillKill()
#   * test_newOrder_btcusd_stopPrice()
#
def test_newOrder_btcusd_clientOrderId():
        print(end='\n')
        print(end='\n')
        print("##########  Executing Positive test suite where symbol = btcusd, with optional parameters ##########")
        print(end='\n')          
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test1",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["maker-or-cancel"],
                "stop_price": "999.00"
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()       
        print("Test Result: test_newOrder_btcusd_clientOrderId()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        print(end='\n')

def test_newOrder_btcusd_minAmount():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test1",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["maker-or-cancel"],
                "stop_price": "999.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print(end='\n')
        print("Test Result: test_newOrder_btcusd_minAmount()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        print(end='\n')

def test_newOrder_btcusd_OptionsMakerCancel():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test1",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["maker-or-cancel"],
                "stop_price": "999.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print("Test Result: test_newOrder_btcusd_OptionsMakerCancel()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        print(end='\n')

def test_newOrder_btcusd_OptionsImmediateCancel():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test1",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["immediate-or-cancel"],
                "stop_price": "999.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print("Test Result: test_newOrder_btcusd_OptionsImmediateCancel()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        print(end='\n')

def test_newOrder_btcusd_OptionsFillKill():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test1",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["fill-or-kill"],
                "stop_price": "999.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print("Test Result: test_newOrder_btcusd_OptionsFillKill()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        print(end='\n')

def test_newOrder_btcusd_stopPrice():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test1",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["maker-or-cancel"],
                "stop_price": "777.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print("Test Result: test_newOrder_btcusd_stopPrice()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        print(end='\n')

#
# Negative Test suite containing following test cases, with all optional parameters:
#   * test_newOrder_btcusd_OptionsAuctionOnly()
#   * test_newOrder_btcusd_IndicationInterest()
#
def test_newOrder_btcusd_OptionsAuctionOnly():
        print(end='\n')
        print(end='\n')
        print("##########  Executing Negative test suite, with optional parameters ##########")
        print("  ~~~~~~~~~~  NOTE:  Expecting error messages in the results  ~~~~~~~~~~")
        print(end='\n')          
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test2",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["auction-only"],
                "stop_price": "999.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print("Test Result: test_newOrder_btcusd_OptionsAuctionOnly()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)           
        print(end='\n')

def test_newOrder_btcusd_OptionsIndicationInterest():
        time.sleep(1)  # Nonce can't be repeated and can be increased in one session
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test2",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "buy",
                "type": "exchange limit",
                "options": ["indication-of-interest"],
                "stop_price": "999.00"                
        }        
        gemini_NewOrderOptionParms, response = gemini_PostAPI_NewOrder_OptionParms(payloadData).newOrder_optionParms()
        print("Test Result: test_newOrder_btcusd_OptionsIndicationInterest()")
        print(end='\n')        
        print(gemini_NewOrderOptionParms)
        assert response.status_code != HTTP_SUCCESS
        print("Status code = ", response.status_code)  
        print(end='\n')

#
# Negative Test suite containing following test cases, to test Nonce with no increase:
#   * test_newOrder_btcusd_nonceNoIncrease1()
#   * test_newOrder_btcusd_nonceNoIncrease2()
#   * test_newOrder_btcusd_nonceNoIncrease3()
#   * test_newOrder_btcusd_nonceNoIncrease4()
#
def test_newOrder_btcusd_nonceNoIncrease1():
        print(end='\n') 
        print("##########  Executing Negative test suite where the Nonce is not increasing ##########")
        print("  ~~~~~~~~~~  NOTE:  Expecting some 'InvalidNonce' reason in the results  ~~~~~~~~~~")
        print(end='\n')
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test3",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "sell",
                "type": "exchange limit",
                "options": ["maker-or-cancel"]
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_nonceNoIncrease1()")
        print(end='\n')        
        print(gemini_NewOrder)
        print(end='\n')

def test_newOrder_btcusd_nonceNoIncrease2():
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test3",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "sell",
                "type": "exchange limit",
                "options": ["maker-or-cancel"]
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_nonceNoIncrease2()")
        print(end='\n')
        print(gemini_NewOrder)
        print(end='\n')

def test_newOrder_btcusd_nonceNoIncrease3():
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test3",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "sell",
                "type": "exchange limit",
                "options": ["maker-or-cancel"]
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_nonceNoIncrease3()")
        print(end='\n')
        print(gemini_NewOrder)     
        print(end='\n')

def test_newOrder_btcusd_nonceNoIncrease4():
        payloadData = {
                "request": "",
                "nonce": "",
                "client_order_id": "Lila_Test3",
                "symbol": "btcusd",
                "amount": "5",
                "min_amount": "2",
                "price": "3633.00",
                "side": "sell",
                "type": "exchange limit",
                "options": ["maker-or-cancel"]
        }        
        gemini_NewOrder, response = gemini_PostAPI_NewOrder(payloadData).newOrder_Post()
        print("Test Result: test_newOrder_btcusd_nonceNoIncrease4()")
        print(end='\n')
        print(gemini_NewOrder)      
        print(end='\n')




