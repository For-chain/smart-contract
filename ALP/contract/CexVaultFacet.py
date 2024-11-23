#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../../openzeppelin")
sys.path.append("/")

from web3 import Web3, HTTPProvider
from config import *
from ApolloxLP.abi import CexVaultFacet_abi

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
CexVaultFacet = w3.eth.contract(address=APOLLOX_CONTRACT_TEST, abi=CexVaultFacet_abi.abi)


def maxWithdrawAbleUsd():
    result = CexVaultFacet.caller().maxWithdrawAbleUsd()
    return result
    # print(result)


def securityMarginRate():
    result = CexVaultFacet.caller().securityMarginRate()
    return result

