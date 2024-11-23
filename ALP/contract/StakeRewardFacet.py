#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../../openzeppelin")
sys.path.append("/")

from web3 import Web3, HTTPProvider
from config import *
from ApolloxLP.abi import StakeRewardFacet_abi

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
StakeRewardFacet = w3.eth.contract(address=APOLLOX_CONTRACT_TEST, abi=StakeRewardFacet_abi.abi)


def totalStaked():
    result = StakeRewardFacet.caller().totalStaked()
    print('Total Staked ALP: '+str(result/10**18))
    return result


def stakeOf(address):
    result = StakeRewardFacet.caller().stakeOf(address)
    print(address+' Staked ALP: ' + str(result / 10 ** 18))
    return result


def stake(privateKey, nonce, amount):
    amount = w3.to_wei(amount, 'ether')
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = StakeRewardFacet.functions.stake(amount)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def unStake(privateKey, nonce, amount):
    amount = w3.to_wei(amount, 'ether')
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = StakeRewardFacet.functions.unStake(amount)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def claimAllReward(privateKey, nonce):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = StakeRewardFacet.functions.claimAllReward()
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)
