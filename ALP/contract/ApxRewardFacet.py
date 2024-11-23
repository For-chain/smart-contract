#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../../ALP")
sys.path.append("../../openzeppelin")
sys.path.append("/")

from web3 import Web3, HTTPProvider
from config import *
from ApolloxLP.abi import ApxRewardFacet_abi


w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
ApxRewardFacet = w3.eth.contract(address=APOLLOX_CONTRACT_TEST, abi=ApxRewardFacet_abi.abi)


def apxPoolInfo():
    result = ApxRewardFacet.caller().apxPoolInfo()
    result = list(result)
    for i in range(0, len(result)):
        if i == 2:
            continue
        elif i == 3:
            result[i] = result[i] / 10 ** 12
            continue
        result[i] = result[i] / 10 ** 18
    return result
    # print(result)


def pendingApx(address):
    print('Current block is ' + str(w3.eth.blockNumber))
    result = ApxRewardFacet.caller().pendingApx(address) / 10 ** 18
    print(result)


def addReserves(privateKey, nonce, amount):
    amount = w3.to_wei(amount, 'ether')
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = ApxRewardFacet.functions.addReserves(amount)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)


def updateApxPerBlock(privateKey, nonce, apxPerBlock):
    amount = w3.to_wei(apxPerBlock, 'ether')
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = ApxRewardFacet.functions.updateApxPerBlock(amount)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)


