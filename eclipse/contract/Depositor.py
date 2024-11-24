#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from web3 import Web3, HTTPProvider
from config import *

class Depositor:
    def __init__(self, w3, depositor, gas_price_gwei):
        self.w3 = w3
        self.depositor = depositor
        self.gas_price_gwei = gas_price_gwei

    def deposit(self, privateKey, nonce, value, target, token, maker, amount, destination, channel):
        value = value * 10 ** 18
        amount = amount * 10 ** 18
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
            'value': int(value)
        }
        func = self.depositor.functions.deposit(target, token, maker, int(amount), destination, channel)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(Web3.to_hex(tx_hash))


