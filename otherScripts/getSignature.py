from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3, HTTPProvider
import requests
import csv
import json
from config import *
import logging

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))

'''日志打印到控制台'''
logger = logging.getLogger('example_logger')
logger.setLevel(logging.INFO)  # 设置最低的日志级别为INFO

# 创建控制台处理程序，并设置日志级别为INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建日志格式器，并将其添加到控制台处理程序
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 将控制台处理程序添加到日志记录器
logger.addHandler(console_handler)

def create_signature(w3, nonce):
    msg = f'You are signing into ApolloX Finance Trading {nonce}'
    message_hash = encode_defunct(text=msg)
    wallet = w3.eth.account.from_key(WALLET_PRIVATE_KEY_1)
    signed_message = wallet.sign_message(message_hash)
    logger.info(f'Message: {msg}')
    logger.info(f'Message Hash: {message_hash}')
    logger.info(f'Signature: {signed_message.signature.hex()}')
    # recovered_address = w3.eth.account._recover_hash(message_hash, signature=signed_message.signature.hex())
    # recovered_address = w3.eth.account._recover_hash(message_hash, signature='0x7d34c854580dd6174787e6f43ea24291743ba56830742db533a6e799f2bf61bd17c95a7b5ea66f0889cf86e97fa3bf4a2515f5feaf54a5165dfbc6b859c451261b')
    # logger.info(f'Recovered_address: {recovered_address}')


if __name__ == '__main__':
    create_signature(w3, 234567)

