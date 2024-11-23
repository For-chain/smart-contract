#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from web3 import Web3, HTTPProvider
from config import *
# from ApolloxLP.abi import Perp_abi

sys.path.append("../../openzeppelin")


class Apollox:
    def __init__(self, w3, apollox, gas_price_gwei):
        self.w3 = w3
        self.apollox = apollox
        self.gas_price_gwei = gas_price_gwei

    def openMarketTrade(self, privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit,
                        broker):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        elif tokenIn in TOKENS_DECIMAL_8:
            amountIn = amountIn * 10 ** 8
        else:
            amountIn = amountIn * 10 ** 18
        open_data_input = (pairBase, isLong, tokenIn, int(amountIn), int(qty * 10 ** 10), int(price * 10 ** 8),
                           int(stopLoss * 10 ** 8), int(takeProfit * 10 ** 8), broker)
        print(open_data_input)
        func = self.apollox.functions.openMarketTrade(open_data_input)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(receipt)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        # trade_hash = Web3.to_hex(receipt['logs'][2]['topics'][1])
        # return trade_hash

    def swapAndOpenMarketTrade(self, privateKey, nonce, swapData, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit,
                        broker):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        elif tokenIn in TOKENS_DECIMAL_8:
            amountIn = amountIn * 10 ** 8
        else:
            amountIn = amountIn * 10 ** 18
        open_data_input = (pairBase, isLong, tokenIn, int(amountIn), int(qty * 10 ** 10), int(price * 10 ** 8),
                           int(stopLoss * 10 ** 8), int(takeProfit * 10 ** 8), broker)
        print(open_data_input)
        func = self.apollox.functions.swapAndOpenMarketTrade(swapData, open_data_input)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))


    def openMarketTradeBNB(self, privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss,
                           takeProfit,
                           broker):
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
            'value': int(amountIn)
        }
        open_data_input = (pairBase, isLong, tokenIn, int(amountIn), int(qty * 10 ** 10), int(price * 10 ** 8),
                           int(stopLoss * 10 ** 8), int(takeProfit * 10 ** 8), broker)

        func = self.apollox.functions.openMarketTradeBNB(open_data_input)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        print(Web3.to_hex(tx_hash))

    def openMarketTradeAndCallback(self, privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss,
                                   takeProfit,
                                   broker, callbackPrice):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        open_data_input = (pairBase, isLong, tokenIn, int(amountIn), int(qty * 10 ** 10), int(price * 10 ** 8),
                           int(stopLoss * 10 ** 8), int(takeProfit * 10 ** 8), broker)

        func = self.apollox.functions.openMarketTrade(open_data_input)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # get requestId
        request_id = Web3.to_hex(receipt['logs'][2]['topics'][1])
        print('request_id: ' + request_id)
        self.requestPriceCallback(privateKey, nonce + 1, request_id, callbackPrice)

    def requestPriceCallback(self, privateKey, nonce, requestId, price):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.requestPriceCallback(requestId, int(price * 10 ** 8))
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def pythRequestPriceCallback(self, privateKey, nonce, requestId, priceId, priceUpdateData):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.requestPriceCallback(requestId, priceId, priceUpdateData)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def executeLimitOrder(self, privateKey, nonce, executeOrders):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.executeLimitOrder(executeOrders)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def pythExecuteLimitOrder(self, privateKey, nonce, KeeperExecutionWithPyth):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.executeLimitOrder(KeeperExecutionWithPyth)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def batchRequestPriceCallback(self, privateKey, nonce, PriceCallbackParam):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.batchRequestPriceCallback(PriceCallbackParam)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def pythBatchRequestPriceCallback(self, privateKey, nonce, PriceCallbackPythParam):
        params = {
            'gas': 5000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.batchRequestPriceCallback(PriceCallbackPythParam)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def batchRequestPriceCallbackAll(self, privateKey, nonce, PriceCallbackPythParam, priceUpdateData):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.batchRequestPriceCallback(PriceCallbackPythParam, priceUpdateData)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def openLimitOrder(self, privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss, takeProfit,
                       broker):
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce
        }
        open_data_input = (pairBase, isLong, tokenIn, int(amountIn), int(qty * 10 ** 10), int(price * 10 ** 8),
                           int(stopLoss * 10 ** 8), int(takeProfit * 10 ** 8), broker)

        func = self.apollox.functions.openLimitOrder(open_data_input)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        print(Web3.to_hex(tx_hash))

    def openLimitOrderBNB(self, privateKey, nonce, pairBase, isLong, tokenIn, amountIn, qty, price, stopLoss,
                          takeProfit,
                          broker):
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
            'value': int(amountIn)
        }
        open_data_input = (pairBase, isLong, tokenIn, int(amountIn), int(qty * 10 ** 10), int(price * 10 ** 8),
                           int(stopLoss * 10 ** 8), int(takeProfit * 10 ** 8), broker)

        func = self.apollox.functions.openLimitOrderBNB(open_data_input)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        # print(Web3.to_hex(receipt['logs'][2]['topics'][1]))
        print(Web3.to_hex(tx_hash))

    def updateOrderTp(self, privateKey, nonce, orderHash, takeProfit):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        takeProfit = int(takeProfit * 10 ** 8)
        func = self.apollox.functions.updateOrderTp(orderHash, takeProfit)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updateTradeTp(self, privateKey, nonce, tradeHash, takeProfit):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        takeProfit = int(takeProfit * 10 ** 8)
        func = self.apollox.functions.updateTradeTp(tradeHash, takeProfit)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updateOrderSl(self, privateKey, nonce, orderHash, stopLoss):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        stopLoss = int(stopLoss * 10 ** 8)
        func = self.apollox.functions.updateOrderSl(orderHash, stopLoss)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updateTradeSl(self, privateKey, nonce, tradeHash, stopLoss):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        stopLoss = int(stopLoss * 10 ** 8)
        func = self.apollox.functions.updateTradeSl(tradeHash, stopLoss)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updateOrderTpAndSl(self, privateKey, nonce, orderHash, takeProfit, stopLoss):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        takeProfit = int(takeProfit * 10 ** 8)
        stopLoss = int(stopLoss * 10 ** 8)
        func = self.apollox.functions.updateOrderTpAndSl(orderHash, takeProfit, stopLoss)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updateTradeTpAndSl(self, privateKey, nonce, orderHash, takeProfit, stopLoss):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        takeProfit = int(takeProfit * 10 ** 8)
        stopLoss = int(stopLoss * 10 ** 8)
        func = self.apollox.functions.updateTradeTpAndSl(orderHash, takeProfit, stopLoss)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updatePairPositionInfo(self, privateKey, nonce, pairBase):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.updatePairPositionInfo(pairBase)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def closeTrade(self, privateKey, nonce, tradeHash):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.closeTrade(tradeHash)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def batchCloseTrade(self, privateKey, nonce, tradeHashes):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.batchCloseTrade(tradeHashes)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def predictAndBet(self, privateKey, nonce, pairBase, isUp, period, tokenIn, amountIn, price, broker):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        PredictionInput = (pairBase, isUp, period, tokenIn, int(amountIn), int(price * 10 ** 8), broker)

        func = self.apollox.functions.predictAndBet(PredictionInput)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def predictAndBetBNB(self, privateKey, nonce, pairBase, isUp, period, tokenIn, amountIn, price, broker):
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
            'value': int(amountIn)
        }
        PredictionInput = (pairBase, isUp, period, tokenIn, int(amountIn), int(price * 10 ** 8), broker)

        func = self.apollox.functions.predictAndBetBNB(PredictionInput)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def settlePredictions(self, privateKey, nonce, SettlePrediction):
        params = {
            'gas': 2500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }

        func = self.apollox.functions.settlePredictions(SettlePrediction)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def settlePredictionsWithPyth(self, privateKey, nonce, SettlePredictionWithPyth):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }

        func = self.apollox.functions.settlePredictions(SettlePredictionWithPyth)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def executeTpSlOrLiq(self, privateKey, nonce, TpSlOrLiq):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }

        func = self.apollox.functions.executeTpSlOrLiq(TpSlOrLiq)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def executeTpSlOrLiqWithPyth(self, privateKey, nonce, TpSlOrLiqWithPyth):
        params = {
            'gas': 1500000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }

        func = self.apollox.functions.executeTpSlOrLiq(TpSlOrLiqWithPyth)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def addPair(self, privateKey, nonce, base, name, pairType, status, slippageConfigIndex, feeConfigIndex,
                longHoldingFeeRate, shortHoldingFeeRate, pairConfig=None, leverageMargins=None):
        params = {
            'gas': 3000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if pairConfig == None:
            pairConfig = [int(3000000 * 10 ** 18), int(3000000 * 10 ** 18), 0, 1700000000, 41000000000]
        if leverageMargins == None:
            leverageMargins = [(int(3000000 * 10 ** 18), 1, 20, 8500, 9000)]
        func = self.apollox.functions.addPair(base, name, pairType, status, pairConfig, slippageConfigIndex,
                                              feeConfigIndex, leverageMargins, longHoldingFeeRate, shortHoldingFeeRate)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def setMaxTpRatioForLeverage(self, privateKey, nonce, pairBase, maxTpRatios=None):
        if maxTpRatios == None:
            maxTpRatios = []

        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }

        func = self.apollox.functions.setMaxTpRatioForLeverage(pairBase, maxTpRatios)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def addMarginPoolBalance(self, privateKey, nonce, tokenIn, amountIn):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = int(amountIn * 10 ** 6)
        elif tokenIn in TOKENS_DECIMAL_8:
            amountIn = amountIn * 10 ** 8
        else:
            amountIn = int(amountIn * 10 ** 18)
        if tokenIn in TOKENS_ORIGIN:
            params['value'] = amountIn
        func = self.apollox.functions.addMarginPoolBalance(tokenIn, int(amountIn))
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def addMargin(self, privateKey, nonce, tokenIn, tradeHash, amountIn):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = int(amountIn * 10 ** 6)
        elif tokenIn in TOKENS_DECIMAL_8:
            amountIn = amountIn * 10 ** 8
        else:
            amountIn = int(amountIn * 10 ** 18)
        if tokenIn in TOKENS_ORIGIN:
            params['value'] = amountIn
        func = self.apollox.functions.addMargin(tradeHash, int(amountIn))
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print(receipt)

    def addSlippageConfig(self, privateKey, nonce, name, index, onePercentDepthAboveUsd, onePercentDepthBelowUsd,
                          slippageLongP,
                          slippageShortP, longThresholdUsd, shortThresholdUsd, slippageType):
        params = {
            'gas': 3000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        sc = (onePercentDepthAboveUsd, onePercentDepthBelowUsd, slippageLongP, slippageShortP, longThresholdUsd,
              shortThresholdUsd, slippageType)
        func = self.apollox.functions.addSlippageConfig(name, index, sc)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def addFreeBurnWhitelist(self, privateKey, nonce, account):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.addFreeBurnWhitelist(account)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def removeFreeBurnWhitelist(self, privateKey, nonce, account):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.removeFreeBurnWhitelist(account)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def mintAlp(self, privateKey, nonce, tokenIn, amount, minAlp, stake):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if tokenIn in TOKENS_DECIMAL_6:
            amount = int(amount * 10 ** 6)
        else:
            amount = int(amount * 10 ** 18)
        func = self.apollox.functions.mintAlp(tokenIn, amount, minAlp, stake)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def mintAlpWithSignature(self, privateKey, nonce, amount, minAlp, stake, message, signature):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        tokenIn = self.w3.to_checksum_address("0x" + message[154:194])
        if tokenIn in TOKENS_DECIMAL_6:
            amount = int(amount * 10 ** 6)
        elif tokenIn in TOKENS_DECIMAL_8:
            amount = int(amount * 10 ** 8)
        else:
            amount = int(amount * 10 ** 18)
        if tokenIn in TOKENS_ORIGIN:
            params['value'] = amount
            print(params)
        func = self.apollox.functions.mintAlpWithSignature(amount, minAlp, stake, message, signature)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def burnAlpWithSignature(self, privateKey, nonce, alpAmount, minOut, receiver, message, signature):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        alpAmount = self.w3.to_wei(alpAmount, 'ether')
        minOut = self.w3.to_wei(minOut, 'ether')
        func = self.apollox.functions.burnAlpWithSignature(alpAmount, minOut, receiver, message, signature)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def mintAlpBNB(self, privateKey, nonce, amount, minAlp, stake):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
            'value': int(amount * 10 ** 18)
        }
        func = self.apollox.functions.mintAlpBNB(minAlp, stake)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def setSigner(self, privateKey, nonce, signer):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce
        }
        func = self.apollox.functions.setSigner(signer)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def removeBroker(self, privateKey, nonce, id):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.removeBroker(id)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def grantRole(self, privateKey, nonce, role, account):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.grantRole(role, account)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def burnAlp(self, privateKey, nonce, tokenOut, alpAmount, minOut, receiver):
        alpAmount = self.w3.to_wei(alpAmount, 'ether')
        minOut = self.w3.to_wei(minOut, 'ether')
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.burnAlp(tokenOut, alpAmount, minOut, receiver)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def burnAlpBNB(self, privateKey, nonce, alpAmount, minOut, receiver):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce
        }
        alpAmount = alpAmount * 10 ** 18
        func = self.apollox.functions.burnAlpBNB(int(alpAmount), minOut, receiver)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def batchUpdatePairFundingFeeConfig(self, privateKey, nonce, UpdatePairFundingFeeConfigParam=None):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if UpdatePairFundingFeeConfigParam is None:
            UpdatePairFundingFeeConfigParam = [(OPBNB_BTC_TEST, 90867579908, 11000000000, 295000000000)]

        func = self.apollox.functions.batchUpdatePairFundingFeeConfig(UpdatePairFundingFeeConfigParam)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updatePairFundingFeeConfig(self, privateKey, nonce, base, fundingFeePerBlockP, minFundingFeeR, maxFundingFeeR):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.updatePairFundingFeeConfig(base, fundingFeePerBlockP, minFundingFeeR,
                                                                 maxFundingFeeR)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def batchUpdateSlippageConfig(self, privateKey, nonce, UpdateSlippageConfigParam=None):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if UpdateSlippageConfigParam is None:
            UpdateSlippageConfigParam = [(0, 0, 401190220000000000000000000, 401190220000000000000000000, 1, 1,
                                          100000000000000000000000, 100000000000000000000000),
                                         (1, 0, 401190220000000000000000000, 401190220000000000000000000, 1, 1,
                                          100000000000000000000000, 100000000000000000000000),
                                         (2, 0, 401190220000000000000000000, 401190220000000000000000000, 1, 1,
                                          100000000000000000000000, 100000000000000000000000)]

        func = self.apollox.functions.batchUpdateSlippageConfig(UpdateSlippageConfigParam)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updatePredictionPairMaxCap(self, privateKey, nonce, base, periodCaps=None):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if periodCaps is None:
            periodCaps = [[1, 10000000000000000000000, 10000000000000000000000]]
        func = self.apollox.functions.updatePredictionPairMaxCap(base, periodCaps)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def setExecutionFeeReceiver(self, privateKey, nonce, receiver):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.setExecutionFeeReceiver(receiver)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def addPartner(self, privateKey, nonce, name, url, protocolAddress, callbackReceiver):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.addPartner(name, url, protocolAddress, callbackReceiver)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updatePartnerName(self, privateKey, nonce, protocolAddress, name):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.updatePartnerName(protocolAddress, name)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updatePartnerUrl(self, privateKey, nonce, protocolAddress, url):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.updatePartnerUrl(protocolAddress, url)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def updatePartnerCallbackReceiver(self, privateKey, nonce, protocolAddress, callbackReceiver):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        func = self.apollox.functions.updatePartnerCallbackReceiver(protocolAddress, callbackReceiver)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def safeMode(self, privateKey, nonce, openSafeMode, bases, updateLeverages=None):
        params = {
            'gas': 2000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        if updateLeverages == None:
            updateLeverages = [[BSC_BTC_TEST, [(int(3000000 * 10 ** 18), 1, 250, 8500, 9000)]]]
        func = self.apollox.functions.safeMode(openSafeMode, bases, updateLeverages)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def setOneInchAggregationRouter(self, privateKey, nonce, oneInchAggregationRouter):
        params = {
            'gas': 1000000,
            'gasPrice': self.w3.to_wei(self.gas_price_gwei, 'gwei'),
            'nonce': nonce,
        }
        oneInchAggregationRouter = self.w3.to_checksum_address(oneInchAggregationRouter)
        func = self.apollox.functions.setOneInchAggregationRouter(oneInchAggregationRouter)
        tx = func.build_transaction(params)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(Web3.to_hex(tx_hash))

    def getTokenByAddress(self, tokenAddress):
        result = self.apollox.caller().getTokenByAddress(tokenAddress)
        return result

    def lpUnrealizedPnlUsd(self, targetToken=None):
        if targetToken is None:
            result = self.apollox.caller().lpUnrealizedPnlUsd()
        else:
            result = self.apollox.caller().lpUnrealizedPnlUsd(targetToken)
        return result

    def ALP(self):
        result = self.apollox.caller().ALP()
        return result

    def alpPrice(self):
        result = self.apollox.caller().alpPrice()
        return result

    def chainlinkPriceFeeds(self):
        result = self.apollox.caller().chainlinkPriceFeeds()
        return result

    def getMarketInfo(self, pairBase):
        result = self.apollox.caller().getMarketInfo(pairBase)
        return result

    def getPairQty(self, pairBase):
        result = self.apollox.caller().getPairQty(pairBase)
        return result

    def getPositionByHashV2(self, tradeHash):
        result = self.apollox.caller().getPositionByHashV2(tradeHash)
        return result

    def slippagePrice(self, pairBase, marketPrice, qty, isLong):
        marketPrice = int(marketPrice * 10 ** 8)
        qty = int(qty * 10 ** 10)
        result = self.apollox.caller().slippagePrice(pairBase, marketPrice, qty, isLong)
        return result

    def executeLimitOrderCheck(self, user, userOpenOrderIndex, limitPrice, pairBase, amountIn, tokenIn, isLong,
                               stopLoss, qty, takeProfit, marketPrice, broker=1, timestamp=1709812383):
        if tokenIn in TOKENS_DECIMAL_6:
            amountIn = amountIn * 10 ** 6
        else:
            amountIn = amountIn * 10 ** 18
        limitPrice, stopLoss, takeProfit, marketPrice, qty = int(limitPrice * 10 ** 8), int(stopLoss * 10 ** 8), int(
            takeProfit * 10 ** 8), int(marketPrice * 10 ** 8), int(qty * 10 ** 10)
        order = (
        user, userOpenOrderIndex, limitPrice, pairBase, amountIn, tokenIn, isLong, broker, stopLoss, qty, takeProfit,
        timestamp)
        result = self.apollox.caller().executeLimitOrderCheck(order, marketPrice)
        return result

    def traderAssets(self, tokens):
        result = self.apollox.caller().traderAssets(tokens)
        return result

    def itemValue(self, token):
        result = self.apollox.caller().itemValue(token)
        return result
