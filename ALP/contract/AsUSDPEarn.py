# -*- coding: utf-8 -*-

import sys
import os
from web3 import Web3, HTTPProvider
from config import *
from decimal import Decimal, getcontext

sys.path.append("../../openzeppelin")
sys.path.append("/")

class AsUSDPEarn:
    def __init__(self, w3, earn, gas_price_gwei):
        self.w3 = w3
        self.earn = earn
        self.gas_price_gwei = gas_price_gwei

    getcontext().prec = 18

    def deposit(self, privateKey, nonce, USDTAddress, amountIn):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if amountIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        elif amountIn in TOKENS_DECIMAL_8:
            amountIn = amountIn * 10 ** 8
        else:
            amountIn = Decimal(amountIn) * Decimal(10 ** 18)
        func = self.earn.functions.deposit(USDTAddress, int(amountIn))
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))
        # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(receipt)

    def initialize(self, privateKey, nonce, defaultAdmin):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.earn.functions.initialize(defaultAdmin)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def transferToCeffu(self, privateKey, nonce):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.earn.functions.transferToCeffu()
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))



