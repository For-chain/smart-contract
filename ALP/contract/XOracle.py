#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../../openzeppelin")
sys.path.append("/")

from web3 import Web3, HTTPProvider
from config import *
from ApolloxLP.abi import XOracle_abi

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
XOracle = w3.eth.contract(address=ALP_ORACLE_CONTRACT_TEST, abi=XOracle_abi.abi)


def getRecordsAtIndex(index):
    result = XOracle.caller().getRecordsAtIndex(index)
    return result
    # print(result)

