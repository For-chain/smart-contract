import sys
import os


from ALP.abi import Perp_abi
from ALP.contract import Apollox
from web3 import Web3, HTTPProvider
from config import *


w3 = Web3(HTTPProvider(BASE_RPC_URL_TEST))
apollox = w3.eth.contract(address=BASE_APOLLOX_CONTRACT_TEST, abi=Perp_abi.abi)

nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)
# nonce_2 = w3.eth.get_transaction_count(WALLET_ADDRESS_2)
# nonce_3 = w3.eth.get_transaction_count(WALLET_ADDRESS_3)
# nonce_4 = w3.eth.get_transaction_count(WALLET_ADDRESS_4)
# nonce_5 = w3.eth.get_transaction_count(WALLET_ADDRESS_5)

perp = Apollox.Apollox(w3, apollox, BASE_GWEI_TEST)

# for role in [DEFAULT_ADMIN_ROLE, PAIR_OPERATOR_ROLE, PRICE_FEED_OPERATOR_ROLE]:
#     perp.grantRole(WALLET_PRIVATE_KEY_1, nonce_1, role, '0x57CbbC7f0cc50cB3a80D1b7f6B541bb2EDB0C25B')
#     nonce_1 += 1

# perp.addPair(WALLET_PRIVATE_KEY_1, nonce_1, BASE_WETH_TEST, 'ETH/USD', 0, 0,0,0,9500,9500)

# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BASE_WETH_TEST, False, BASE_USDC_TEST, 10, 0.1, 1950, 0, 1900, 1)
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_TEST, True, BASE_USDC_TEST, 100, 0.1, 38000, 0, 39000, 1)
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BASE_500BTC_TEST, False, BASE_USDC_TEST, 1, 0.012, 37900, 0, 37900, 1)
# perp.openMarketTradeAndCallback(WALLET_PRIVATE_KEY_1, nonce_1, BASE_WETH_TEST, False, BASE_USDC_TEST, 10, 0.1, 1950, 0, 1900, 1, 2019)

# perp.requestPriceCallback(WALLET_PRIVATE_KEY_1, nonce_1, '0x2B2B89416BBC2B3B47F0BDA04E742C4392EA828E22B8F2AA573B518C0D288FAD', 2312)

perp.openLimitOrder(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_TEST, True, BASE_USDC_TEST, 100, 0.1, 52000, 0, 53000, 1)

# perp.addPair(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_TEST, 'BTC/USD', 0, 0, 0, 0, 9500, 9500)

# 查询接口

# print(perp.lpUnrealizedPnlUsd())
# perp.addMargin(WALLET_PRIVATE_KEY_1, nonce_1, BASE_USDC_TEST, '0x1676D03B557E9AC0ACB40F755DE79EAF1AE958F469A00A777C47BFBF7B7C87FF', 10)
# perp.batchUpdateSlippageConfig(WALLET_PRIVATE_KEY_1, nonce_1, [(1, 0, 301190220000000000000000000, 301190220000000000000000000, 1, 1, 200000000000000000000000, 200000000000000000000000)])
# perp.mintAlp(WALLET_PRIVATE_KEY_1, nonce_1, BASE_USDC_TEST, 1, 0, False)
# perp.batchCloseTrade(WALLET_PRIVATE_KEY_1, nonce_1, ['0x4a4bf86535a9102be2a83024aa00f67a716d2a58aa6767ab43ba3b75d06090df'])
# perp.addSlippageConfig(WALLET_PRIVATE_KEY_1, nonce_1, 'type3', 2, 421518274000000000000000000, 421518274000000000000000000, 0, 0, 1000000000000000000000, 1000000000000000000000, 3)
# perp.batchUpdatePairFundingFeeConfig(WALLET_PRIVATE_KEY_1, nonce_1)
# perp.openMarketTradeBNB(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_TEST, False, BSC_USDT_TEST, 0.005, 0.01, 45000, 0, 40000, 1)