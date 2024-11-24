"""owlto跨链，测试发现无法通过直接调用合约方式使用"""

import sys
import os
import time

from abi import owlto_depositor_abi
from contract import Depositor
from web3 import Web3, HTTPProvider
from config import *
from secret import *

w3 = Web3(HTTPProvider(BASE_RPC_URL_MAIN))
depositor = w3.eth.contract(address=BASE_DIPOSITOR, abi=owlto_depositor_abi.abi)

# nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)
nonce_2 = w3.eth.get_transaction_count(SECRET_ADDRESS_2)
# nonce_3 = w3.eth.get_transaction_count(WALLET_ADDRESS_3)
# nonce_4 = w3.eth.get_transaction_count(WALLET_ADDRESS_4)
# nonce_5 = w3.eth.get_transaction_count(WALLET_ADDRESS_5)

bridge = Depositor.Depositor(w3, depositor, BASE_GWEI_MAIN)

bridge.deposit(SECRET_PRIVATE_KEY_2, nonce_2, 0.0004, 'BGSsAcXUvEcFPJkTJFoujh6ETQPkqCa6b7tJyPK4Wmfs', ZERO_ADDRESS,
                 BASE_MAKER, 0.0004, BASE_DESTINATION, BASE_CHANNEL)
