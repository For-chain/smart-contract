#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from web3 import Web3, HTTPProvider
from config import *
from tokens.abi import ERC20_abi

sys.path.append("../../openzeppelin")


class Erc20:
    def __init__(self, w3, erc20, gas_price_gwei):
        self.w3 = w3
        self.erc20 = erc20
        self.gas_price_gwei = gas_price_gwei

    def balanceOf(self, address):
        result = self.erc20.caller().balanceOf(address)
        return result

    def totalSupply(self):
        result = self.erc20.caller().totalSupply() / 10 ** 18
        return result

    def approve(self, privateKey, nonce, tokenContract, spender, amount):
        params = {
            'gas': 100000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.erc20.functions.approve(spender, amount)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print(receipt)

    def transfer(self, privateKey, nonce, to, amount):
        amount = self.w3.to_wei(amount, 'ether')
        params = {
            'gas': 100000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.erc20.functions.transfer(to, amount)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(tx_hash)

    def transferFrom(self, privateKey, nonce, fromAddr, toAddr, amount):
        amount = self.w3.to_wei(amount, 'ether')
        params = {
            'gas': 100000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.erc20.functions.transfer(fromAddr, toAddr, amount)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(tx_hash)

    def burn(self, privateKey, nonce, amount):
        amount = self.w3.to_wei(amount, 'ether')
        params = {
            'gas': 100000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.erc20.functions.burn(amount)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(tx_hash)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(receipt)

