# -*- coding: utf-8 -*-

import sys
import os

sys.path.append("../../openzeppelin")
sys.path.append("/")

from web3 import Web3, HTTPProvider
from config import *
from DepositeAndWithdraw.abi import ApolloxExchangeTreasury_abi

w3 = Web3(HTTPProvider(ARB_RPC_URL_TEST))
arbTreasuryContract = w3.eth.contract(address=ARB_TREASURY_CONTRACT_TESTNET, abi=ApolloxExchangeTreasury_abi.abi)


def withdraw(privateKey, nonce, message, signature):
    params = {
        'gas': 3000000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = arbTreasuryContract.functions.withdraw(message, signature)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def claim(privateKey, nonce, message, signature):
    params = {
        'gas': 3000000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = arbTreasuryContract.functions.claim(message, signature)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)





