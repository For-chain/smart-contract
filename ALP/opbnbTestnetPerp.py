import sys
import os


from ALP.abi import Perp_abi
from ALP.contract import Apollox
from web3 import Web3, HTTPProvider
from config import *


w3 = Web3(HTTPProvider(OPBNB_RPC_URL_TEST))
apollox = w3.eth.contract(address=OPBNB_APOLLOX_CONTRACT_TEST, abi=Perp_abi.abi)

nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)
# nonce_2 = w3.eth.get_transaction_count(WALLET_ADDRESS_2)
# nonce_3 = w3.eth.get_transaction_count(WALLET_ADDRESS_3)
# nonce_4 = w3.eth.get_transaction_count(WALLET_ADDRESS_4)
# nonce_5 = w3.eth.get_transaction_count(WALLET_ADDRESS_5)

perp = Apollox.Apollox(w3, apollox, OPBNB_GWEI_TEST)

# print(perp.lpUnrealizedPnlUsd("0xb444362CB447f4A703596F2a26A98331A43432ce"))

# result = perp.slippagePrice(OPBNB_BTC_TEST, 67876, 1, True)
# print(result)

perp.batchRequestPriceCallback(WALLET_PRIVATE_KEY_1, nonce_1,
                                           [('0x8975CED172CDA6EA801D3C280023C01B4E86EEA5737E11F2470F8B41B93F20FC', int(242 * 10 ** 8)),
                                            ('0xA24064703F5DDB547A9A76EA2EEF3CD8E85E7A60D83431243055C8CB626A5744', int(1975 * 10 ** 8)),
                                            ('0xB6780A2D7185923DD38EDE56AC84BD617E1166B692477256635ACEA5D5B7EA89', int(1970 * 10 ** 8)),
                                            ('0x1DF8D9583E3C2CD38A0DF7CD7B74A1B40BBA013496E9A3C8E2D7BFF5A90B772B', int(241 * 10 ** 8))]
                                           )

# perp.burnAlpWithSignature(WALLET_PRIVATE_KEY_1, nonce_1, 1, 0, WALLET_ADDRESS_1,
#                           "0x00000000000000000000000000000000000000000000000000000000000015eb0000000000000000000000000000000000000000000000000000000065e8ab70000000000000000000000000617d91847b74b70a3d3e3745445cb0d1b3c8560efffffffffffffffffffffffffffffffffffffffffffffeb22ecc79ca96407017ffffffffffffffffffffffffffffffffffffffffffffffffe6c7805256635eb4",
#                           "0xb1069e0d2ab3fd0598b74b9c3659d55d7ef652207031394b56a6a22433b4a8151d228cb465dfdc95961a3a1ccd9e71248e7607acabe790ef830e1f964a8daae81b")

# perp.mintAlpWithSignature(WALLET_PRIVATE_KEY_1, nonce_1, 0.001, 0, True,
#                           "0x00000000000000000000000000000000000000000000000000000000000015eb0000000000000000000000000000000000000000000000000000000065e8ab70000000000000000000000000617d91847b74b70a3d3e3745445cb0d1b3c8560efffffffffffffffffffffffffffffffffffffffffffffeb22ecc79ca96407017ffffffffffffffffffffffffffffffffffffffffffffffffe6c7805256635eb4",
#                           "0xb1069e0d2ab3fd0598b74b9c3659d55d7ef652207031394b56a6a22433b4a8151d228cb465dfdc95961a3a1ccd9e71248e7607acabe790ef830e1f964a8daae81b")

# perp.burnAlpBNB(WALLET_PRIVATE_KEY_1, nonce_1, 10, 0, WALLET_ADDRESS_1)

# perp.mintAlpBNB(WALLET_PRIVATE_KEY_1, nonce_1, 0.5, 0, False)

# perp.mintAlp(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_USDT_TEST, 100, 0, False)

# perp.burnAlp(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_USDT_TEST, 10, 0, WALLET_ADDRESS_1)


# for role in [DEFAULT_ADMIN_ROLE, PAIR_OPERATOR_ROLE, PRICE_FEED_OPERATOR_ROLE]:
#     perp.grantRole(WALLET_PRIVATE_KEY_1, nonce_1, role, '0x57CbbC7f0cc50cB3a80D1b7f6B541bb2EDB0C25B')
#     nonce_1 += 1

# perp.burnAlp(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_USDT_TEST, 1, 0, WALLET_ADDRESS_1)

#token approve
# busd_token = w3.eth.contract(address=BSC_BUSD_TOKEN_TESTNET, abi=ERC20_abi.abi)
# ERC20.approve(WALLET_PRIVATE_KEY_3, nonce_3, busd_token, APOLLOX_CONTRACT_TEST, MAX_AMOUNT)
# ERC20.approve(WALLET_PRIVATE_KEY_4, nonce_4, busd_token, APOLLOX_CONTRACT_TEST, MAX_AMOUNT)
# ERC20.approve(WALLET_PRIVATE_KEY_5, nonce_5, busd_token, APOLLOX_CONTRACT_TEST, MAX_AMOUNT)

# TradingPortalFacet.setTradingSwitches(WALLET_PRIVATE_KEY_2, nonce_2, True, True, True, True, True, True)

# 市价单下单
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_BTC_TEST, True, OPBNB_USDT_TEST, 10, 0.01, 42000, 0, 42000, 1)
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_500BTC_TEST, True, OPBNB_USDT_TEST, 1, 0.01, 41900, 0, 41900, 1)
# perp.openMarketTradeBNB(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_BTC_TEST, False, OPBNB_WBNB_TEST, 0.01, 0.01, 37000, 0, 37000, 1)

# 限价单下单
# perp.openLimitOrder(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_BTC_TEST, True, OPBNB_USDT_TEST, 100,0.01, 51620, 0, 52000, 1)

# 平仓
# perp.closeTrade(WALLET_PRIVATE_KEY_1, nonce_1, '0x02eadf49442743acdd86849669911fd1cfde88f210f237678285ae5b8fde3df4')

# 手动添加保证金池子金额
# perp.addMarginPoolBalance(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_ETH_TEST, 1)

# 预测
# perp.predictAndBet(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_BTC_TEST, False, 0, OPBNB_USDT_TEST, 24, 35000, 1)

# 修改配置
# perp.addPair(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_500BTC_TEST, '500BTC/USD', 0, 0, 1, 1, 9500, 9500)
# perp.setMaxTpRatioForLeverage(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_500BTC_TEST)
# perp.addFreeBurnWhitelist(WALLET_PRIVATE_KEY_1, nonce_1, WALLET_ADDRESS_1)
# perp.removeFreeBurnWhitelist(WALLET_PRIVATE_KEY_1, nonce_1, WALLET_ADDRESS_1)


# 开仓callback
# perp.openMarketTradeAndCallback(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_BTC_TEST, True, OPBNB_USDT_TEST, 15, 0.01, 52500, 0, 52600, 1,52279)
# PriceFacadeFacet.batchRequestPriceCallback(WALLET_PRIVATE_KEY_1, nonce_1,
#                                            [('0x8975CED172CDA6EA801D3C280023C01B4E86EEA5737E11F2470F8B41B93F20FC', int(242 * 10 ** 8)),
#                                             ('0xA24064703F5DDB547A9A76EA2EEF3CD8E85E7A60D83431243055C8CB626A5744', int(1975 * 10 ** 8)),
#                                             ('0xB6780A2D7185923DD38EDE56AC84BD617E1166B692477256635ACEA5D5B7EA89', int(1970 * 10 ** 8)),
#                                             ('0x1DF8D9583E3C2CD38A0DF7CD7B74A1B40BBA013496E9A3C8E2D7BFF5A90B772B', int(241 * 10 ** 8))]
#                                            )

# PredictUpDownFacet.settlePredictions(WALLET_PRIVATE_KEY_1, nonce_1, [(307, 37000*10**8)])

# 猜涨跌
# PredictUpDownFacet.predictAndBet(WALLET_PRIVATE_KEY_5, nonce_5, BSC_BTC_TOKEN_TESTNET, False, 0, BSC_USDT_TOKEN_TESTNET, 34, 35000, 1)

# perp.openMarketTradeBNB(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_TEST, False, BSC_USDT_TEST, 0.005, 0.01, 45000, 0, 40000, 1)
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_BTC_TEST, True, OPBNB_USDT_TEST, 50, 0.01, 47000, 0, 47700, 1)

# print(perp.alpPrice())
# perp.addMargin(WALLET_PRIVATE_KEY_1, nonce_1, OPBNB_USDT_TEST, '0x869f20f62fcf4b2fc4be39c87be3df76a4e067a6726ec021e44d15a714074e6a', 20)
# perp.addSlippageConfig(WALLET_PRIVATE_KEY_1, nonce_1, 'type3', 3, 421518274000000000000000000, 421518274000000000000000000, 0, 0, 1000000000000000000000, 1000000000000000000000, 3)

# perp.batchUpdatePairFundingFeeConfig(WALLET_PRIVATE_KEY_1, nonce_1)

# perp.batchUpdateSlippageConfig(WALLET_PRIVATE_KEY_1, nonce_1, [(1, 0, 301190220000000000000000000, 301190220000000000000000000, 1, 1, 200000000000000000000000, 200000000000000000000000)])