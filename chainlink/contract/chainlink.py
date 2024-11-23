#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../../chainlink")
sys.path.append("/")

from web3 import Web3, HTTPProvider
from config import *
from chainlink.abi import EACAggregatorProxy_abi

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))


def getTokenPrice(tokenAddress):
    token_chainlink_list = {BSC_BUSD_TOKEN_TEST: CHAINLINK_BUSDUSD_TEST, BSC_USDT_TOKEN_TEST: CHAINLINK_USDTUSD_TEST, BSC_WBNB_TOKEN_TEST: CHAINLINK_BNBUSD_TEST}
    chainlink_contract = w3.eth.contract(address=token_chainlink_list[tokenAddress], abi=EACAggregatorProxy_abi.abi)
    result = chainlink_contract.caller().latestAnswer()
    return result


def usdtPrice():
    chainlink_usdt_test = w3.eth.contract(address=CHAINLINK_USDTUSD_TEST, abi=EACAggregatorProxy_abi.abi)
    result = chainlink_usdt_test.caller().latestAnswer()
    return result
    # print(result)


def busdPrice():
    chainlink_busd_test = w3.eth.contract(address=CHAINLINK_BUSDUSD_TEST, abi=EACAggregatorProxy_abi.abi)
    result = chainlink_busd_test.caller().latestAnswer()
    return result
    # print(result)


def bnbPrice():
    chainlink_bnb_test = w3.eth.contract(address=CHAINLINK_BNBUSD_TEST, abi=EACAggregatorProxy_abi.abi)
    result = chainlink_bnb_test.caller().latestAnswer()
    return result
    # print(result)