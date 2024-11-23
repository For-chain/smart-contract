import sys
import os
import time


from ALP.abi import AsUSDPEarn_abi
from ALP.contract import AsUSDPEarn
from web3 import Web3, HTTPProvider
from config import *


w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
earn_contract = w3.eth.contract(address=BSC_USDP_EARN_TEST, abi=AsUSDPEarn_abi.abi)

nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)
# nonce_2 = w3.eth.get_transaction_count(WALLET_ADDRESS_2)
# nonce_3 = w3.eth.get_transaction_count(WALLET_ADDRESS_3)
# nonce_4 = w3.eth.get_transaction_count(WALLET_ADDRESS_4)
# nonce_5 = w3.eth.get_transaction_count(WALLET_ADDRESS_5)

earn = AsUSDPEarn.AsUSDPEarn(w3, earn_contract, BSC_GWEI_TEST)

earn.deposit(WALLET_PRIVATE_KEY_1, nonce_1, BSC_USDT_TEST, 100)
# earn.transferToCeffu(WALLET_PRIVATE_KEY_1, nonce_1)

# earn.initialize(WALLET_PRIVATE_KEY_1, nonce_1, WALLET_ADDRESS_1)


