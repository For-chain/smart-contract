# -*- coding: utf-8 -*-

import sys
import os

from web3 import Web3, HTTPProvider
from config import *
from ALP.abi import ApolloxLP_abi

sys.path.append("../../openzeppelin")
sys.path.append("/")

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
alpContract = w3.eth.contract(address=BSC_ALP_CONTRACT_TEST, abi=ApolloxLP_abi.abi)


def addFromWhiteList(privateKey, nonce, address):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = alpContract.functions.addFromWhiteList(address)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def removeFromWhiteList(privateKey, nonce, address):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = alpContract.functions.removeFromWhiteList(address)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def addToWhiteList(privateKey, nonce, address):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = alpContract.functions.addToWhiteList(address)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def removeToWhiteList(privateKey, nonce, address):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = alpContract.functions.removeToWhiteList(address)
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def pause(privateKey, nonce):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = alpContract.functions.pause()
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)


def unpause(privateKey, nonce):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    }
    func = alpContract.functions.unpause()
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(tx_hash)
    # receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    # print(receipt)
