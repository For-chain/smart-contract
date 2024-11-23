#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from web3 import Web3, HTTPProvider
from config import *
from ApolloxLP.abi import Perp_abi

sys.path.append("../../openzeppelin")


class ApolloxExchangeTreasury:
    def __init__(self, w3, treasury, gas_price_gwei):
        self.w3 = w3
        self.treasury = treasury
        self.gas_price_gwei = gas_price_gwei

    def deposit(self, privateKey, nonce, currency, amount, broker):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if currency in TOKENS_DECIMAL_6:
            amount = amount * 10 ** 6
        elif currency in TOKENS_DECIMAL_8:
            amount = amount * 10 ** 8
        else:
            amount = amount * 10 ** 18

        func = self.treasury.functions.deposit(currency, int(amount), broker)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        print(Web3.to_hex(tx_hash))


    def depositNative(self, privateKey, nonce, amount, broker):
        params = {
            'gas': 1500000,
            'value': int(amount * 10 ** 18),
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }

        func = self.treasury.functions.depositNative(broker)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        print(Web3.to_hex(tx_hash))


    def withdraw(self, privateKey, nonce, message, signature):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.treasury.functions.withdraw(message, signature)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        print(Web3.to_hex(tx_hash))






