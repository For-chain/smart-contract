"""minibridge跨链"""

import sys
import os
import time
import base58

from abi import owlto_depositor_abi
from contract import Depositor
from web3 import Web3, HTTPProvider
from config import *
from secret import *

def transfer_to_bridge(sender_address, private_key, value, eclipse_address):
    value_in_wei = w3.to_wei(value+0.0002, 'ether') + 8847
    # 解码solana地址
    decoded_bytes = base58.b58decode(eclipse_address)
    data = '0x' + str(decoded_bytes.hex())

    # 构建交易
    transaction = {
        'from': sender_address,
        'to': BASE_MINI_BRIDGE,
        'value': value_in_wei,
        'gas': 50000,
        'gasPrice': w3.to_wei(BASE_GWEI_MAIN, 'gwei'),
        'nonce': w3.eth.get_transaction_count(sender_address),
        'chainId': 8453,
        'data': data,  # 附带的自定义数据
    }

    print(f"transaction: {transaction}")

    # 签名交易
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    # 发送交易
    txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"交易已发送，交易哈希: {txn_hash.hex()}")

    # 等待交易确认
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"交易已确认，区块编号: {receipt.blockNumber}")

if __name__ == "__main__":
    w3 = Web3(HTTPProvider(BASE_RPC_URL_MAIN))

    transfer_to_bridge(SECRET_ADDRESS_2, SECRET_PRIVATE_KEY_2, 0.00015, SECRET_ADDRESS_ECLIPSE_1)



