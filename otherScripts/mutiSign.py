"""
并发广播
"""

import sys
import os

sys.path.append("../../chainlink")

import asyncio
import threading
from ALP.abi import Perp_abi
from ALP.contract import Apollox
from web3 import Web3, HTTPProvider
from config import *
from multiprocessing import Process, current_process
from time import sleep

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
apollox = w3.eth.contract(address=BSC_APOLLOX_CONTRACT_TEST, abi=Perp_abi.abi)
perp = Apollox.Apollox(w3, apollox, BSC_GWEI_TEST)

def open_market_trade(privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit, broker, num):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的ID号和名字
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')

    counter, total = 0, num
    print(f'Loop count: {total}, nonce :{nonce}')
    while counter < total:
        perp.openMarketTrade(privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit, broker)
        counter += 1
        nonce += 1

def open_market_trade_callback(privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit, broker, callbackPrice, num):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的ID号和名字
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')

    counter, total = 0, num
    print(f'Loop count: {total}, nonce :{nonce}')
    while counter < total:
        perp.openMarketTradeAndCallback(privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit, broker, callbackPrice)
        counter += 1
        nonce += 1


def predict_and_bet(privateKey, nonce, pairBase, isUp, period, tokenIn, amountIn, price, broker, num):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的ID号和名字
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')

    counter, total = 0, num
    print(f'Loop count: {total}, nonce :{nonce}')
    while counter < total:
        perp.predictAndBet(privateKey, nonce, pairBase, isUp, period, tokenIn, amountIn, price, broker)
        counter += 1
        nonce += 1


def close_trade(privateKey, nonce, tradeHash, num):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的ID号和名字
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')

    counter, total = 0, num
    print(f'Loop count: {total}, nonce :{nonce}')
    while counter < total:
        perp.closeTrade(privateKey, nonce, tradeHash)
        counter += 1
        nonce += 1


def main():
    # nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)
    nonce_4 = w3.eth.get_transaction_count(WALLET_ADDRESS_4)
    nonce_5 = w3.eth.get_transaction_count(WALLET_ADDRESS_5)
    nonce_6 = w3.eth.get_transaction_count(WALLET_ADDRESS_6)
    num = 3
    # 创建并启动进程来执行指定的函数
    # Process(target=close_trade, args=(WALLET_PRIVATE_KEY_5, nonce_5, '0x718262624F41584239C002BE7E85E1CC8B9FC608884161F77A5BA337DE9F5D26', num)).start()
    # Process(target=open_market_trade_callback, args=(WALLET_PRIVATE_KEY_2, nonce_2, BSC_ETH_TEST, True, BSC_USDT_TEST, 100, 0.1, 2800, 0, 2150, 1, 2091, num)).start()
    # Process(target=open_market_trade, args=(WALLET_PRIVATE_KEY_5, nonce_5, BSC_INJ_TEST, True, BSC_USDT_TEST, 10, 20, 21, 0, 21, 1, num)).start()
    Process(target=open_market_trade,
            args=(WALLET_PRIVATE_KEY_4, nonce_4, BSC_WBNB_TEST, True, BSC_USDT_TEST, 5, 0.1, 610, 0, 0, 1, num)).start()
    Process(target=open_market_trade,
            args=(WALLET_PRIVATE_KEY_5, nonce_5, BSC_ETH_TEST, True, BSC_USDT_TEST, 5,  0.01, 2700, 0, 0, 1, num)).start()
    Process(target=open_market_trade,
            args=(WALLET_PRIVATE_KEY_6, nonce_6, BSC_500BTC_TEST, True, BSC_USDT_TEST, 1, 0.01, 66000, 0, 0, 1, num)).start()
    # Process(target=open_market_trade, args=(WALLET_PRIVATE_KEY_2, nonce_2, BSC_ETH_TEST,False, BSC_USDT_TEST, 100, 0.6, 2200, 0, 2100, 1, num)).start()
    # Process(target=predict_and_bet, args=(WALLET_PRIVATE_KEY_1, nonce_1, BSC_BTC_TEST, False, 0, BSC_USDT_TEST, 10, 60000, 1, num)).start()
    # Process(target=predict_and_bet,
    #         args=(WALLET_PRIVATE_KEY_4, nonce_4, BSC_ETH_TEST, False, 0, BSC_USDT_TEST, 20, 2200, 1, num)).start()
    # Process(target=predict_and_bet,
    #         args=(WALLET_PRIVATE_KEY_5, nonce_5, BSC_BTC_TEST, True, 0, BSC_USDT_TEST, 11, 43000, 1, num)).start()
    # open_market_trade(WALLET_PRIVATE_KEY_3, nonce_3, BSC_BTC_TOKEN_TESTNET, False, BSC_USDT_TOKEN_TESTNET, 100, 0.04, 35000, 0, 34500, 1, num)


if __name__ == '__main__':
    main()
