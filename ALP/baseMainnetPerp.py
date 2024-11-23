import sys
import os


from ALP.abi import Perp_abi
from ALP.contract import Apollox
from web3 import Web3, HTTPProvider
from config import *


w3 = Web3(HTTPProvider(BASE_RPC_URL_MAIN))
apollox = w3.eth.contract(address=BASE_APOLLOX_CONTRACT_MAIN, abi=Perp_abi.abi)

# nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)
nonce_2 = w3.eth.get_transaction_count(WALLET_ADDRESS_2)
# nonce_3 = w3.eth.get_transaction_count(WALLET_ADDRESS_3)
# nonce_4 = w3.eth.get_transaction_count(WALLET_ADDRESS_4)
# nonce_5 = w3.eth.get_transaction_count(WALLET_ADDRESS_5)

perp = Apollox.Apollox(w3, apollox, BASE_GWEI_MAIN)

perp.updateTradeTp(WALLET_PRIVATE_KEY_2, nonce_2, "0xce0e763e97c1ecb0ccec30853923fe7cbed68fac1973234e62c76014a5a4c7b7", 70430)

#token approve
# busd_token = w3.eth.contract(address=BSC_BUSD_TOKEN_TESTNET, abi=ERC20_abi.abi)
# ERC20.approve(WALLET_PRIVATE_KEY_3, nonce_3, busd_token, APOLLOX_CONTRACT_TEST, MAX_AMOUNT)
# ERC20.approve(WALLET_PRIVATE_KEY_4, nonce_4, busd_token, APOLLOX_CONTRACT_TEST, MAX_AMOUNT)
# ERC20.approve(WALLET_PRIVATE_KEY_5, nonce_5, busd_token, APOLLOX_CONTRACT_TEST, MAX_AMOUNT)

# TradingPortalFacet.setTradingSwitches(WALLET_PRIVATE_KEY_2, nonce_2, True, True, True, True, True, True)

# 市价单下单
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_MAIN, True, BASE_USDbC_MAIN, 2.5, 0.01, 43200, 0, 43200, 1)
# perp.openMarketTradeBNB(WALLET_PRIVATE_KEY_1, nonce_1, BASE_WETH_MAIN, True, BASE_WETH_MAIN, 0.001, 0.1, 2400, 0, 2500, 1)
# perp.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_MAIN, True, BASE_USDbC_MAIN, 3, 0.01, 43630, 0, 43630, 1)
# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BSC_WBNB_TOKEN_TESTNET, False, BSC_USDT_TOKEN_TESTNET, 100, 0.4, 240, 0, 230, 1)
# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BSC_MADBTC_TOKEN_TESTNET,False, BSC_USDT_TOKEN_TESTNET, 100, 0.4, 370, 0, 300, 1)

# perp.openLimitOrder(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_MAIN, True, BASE_USDbC_MAIN, 3, 0.01, 43800, 43640, 43880, 1)

# 平仓
# perp.closeTrade(WALLET_PRIVATE_KEY_1, nonce_1, '0x497a74f76080ec590b4f7b145395ef542c6e577027811a2ed44494a7da34c368')


# 开仓callback
# PriceFacadeFacet.requestPriceCallback(WALLET_PRIVATE_KEY_1, nonce_1, '0x6B2369B297CD66C6287E226B738D0370FDBB0F2E149A48F85CEC13CD65C289AE', 417)
# PriceFacadeFacet.batchRequestPriceCallback(WALLET_PRIVATE_KEY_1, nonce_1,
#                                            [('0x8975CED172CDA6EA801D3C280023C01B4E86EEA5737E11F2470F8B41B93F20FC', int(242 * 10 ** 8)),
#                                             ('0xA24064703F5DDB547A9A76EA2EEF3CD8E85E7A60D83431243055C8CB626A5744', int(1975 * 10 ** 8)),
#                                             ('0xB6780A2D7185923DD38EDE56AC84BD617E1166B692477256635ACEA5D5B7EA89', int(1970 * 10 ** 8)),
#                                             ('0x1DF8D9583E3C2CD38A0DF7CD7B74A1B40BBA013496E9A3C8E2D7BFF5A90B772B', int(241 * 10 ** 8))]
#                                            )

# PredictUpDownFacet.settlePredictions(WALLET_PRIVATE_KEY_1, nonce_1, [(307, 37000*10**8)])

# 猜涨跌
# perp.predictAndBet(WALLET_PRIVATE_KEY_1, nonce_1, BASE_BTC_MAIN, True, 0, BASE_USDbC_MAIN, 1.01, 45000, 1)

# 计算requestId
# TradingPortalFacet.setMinNotionalUsd(WALLET_PRIVATE_KEY_1, nonce_1, 1)

# TradingPortalFacet.setMaxTakeProfitP(WALLET_PRIVATE_KEY_2, nonce_2, 100000)

# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_1, nonce_1, BSC_BTC_TOKEN_TESTNET, True, ZERO_ADDRESS, 110, 0.1, 23000, 21000, 23500, 1)
# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_2, nonce_2, BSC_BTC_TOKEN_TESTNET, False, BSC_BUSD_TOKEN_TESTNET, 110, 0.1, 21500, 23000, 21000, 1)
# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_3, nonce_3, BSC_BTC_TOKEN_TESTNET, True, BSC_BUSD_TOKEN_TESTNET, 110, 0.1, 23000, 21000, 23500, 1)
# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_4, nonce_4, BSC_BTC_TOKEN_TESTNET, False, BSC_BUSD_TOKEN_TESTNET, 110, 0.1, 21500, 23000, 21000, 1)
# TradingPortalFacet.openMarketTrade(WALLET_PRIVATE_KEY_5, nonce_5, BSC_BTC_TOKEN_TESTNET, True, BSC_BUSD_TOKEN_TESTNET, 110, 0.1, 23000, 21000, 23500, 1)
# PriceFacadeFacet.requestPriceCallback(WALLET_PRIVATE_KEY_1, nonce_1, '0x7a0e09839a42cf13a50c8617a3b01ad91adc6a47990668cef364a883aa8a75e1', 22423.15237143)

# LimitOrderFacet.executeLimitOrder(WALLET_PRIVATE_KEY_1, nonce_1, '0xb891f1d3f6fc6a414dfd388f764467dc7c7047a98af70d0bffcf595871684c81', 22000)
# print(w3.toBytes(hexstr='0xb891f1d3f6fc6a414dfd388f764467dc7c7047a98af70d0bffcf595871684c81'))
# print(PriceFacadeFacet.getPriceFromCacheOrOracle(BSC_BTC_TOKEN_TESTNET)[0]/10 ** 8)
# print(PairsManagerFacet.getPairByBase(BSC_BTC_TOKEN_TESTNET))



#计算requestId

# requestId = w3.keccak(encode_abi(['address', 'uint'], ['0x61110458b8181Aad539A96005Fa773dCee774aF8', 27717961]))
# requestId = w3.toHex(requestId)
# print(requestId)


# VaultFacet.updateAsMagin(WALLET_PRIVATE_KEY_1, nonce_1, BSC_BUSD_TOKEN_TESTNET, True)

# PairsManagerFacet.updatePairStatus(WALLET_PRIVATE_KEY_2, nonce_2, BSC_BTC_TOKEN_TESTNET, 0)

# AccessControlEnumerableFacet.grantRole(WALLET_PRIVATE_KEY_1, nonce_1, PRICE_FEEDER_ROLE, WALLET_ADDRESS_1)

# 限价单下单
# LimitOrderFacet.openLimitOrder(WALLET_PRIVATE_KEY_1, nonce_1, BSC_WBNB_TOKEN_TESTNET, True, BSC_USDT_TOKEN_TESTNET, 50,0.05, 280, 200, 400, 1)
# perp.burnAlpBNB(WALLET_PRIVATE_KEY_1, nonce_1, 1.567267072554602, 0, WALLET_ADDRESS_1)
# perp.burnAlp(WALLET_PRIVATE_KEY_1, nonce_1, BASE_USDbC_MAIN,1.7455091855761150, 0, WALLET_ADDRESS_1)