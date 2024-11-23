"""
批量生成钱包
"""

from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3, HTTPProvider
import requests
import csv
import json
from config import *

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))


def createNewETHWallet():
    wallets = []

    for id in range(10):
        # 添加一些随机性
        account = Account.create('Random Seed'+str(id))

        # 私钥
        privateKey = account._key_obj

        # 公钥
        publicKey = privateKey.public_key

        # 地址
        address = publicKey.to_checksum_address()

        wallet = {
            "id": id,
            "address": address,
            "privateKey": str(privateKey)[2:]
            # "nonce": '',
            # "signature": ''
        }
        wallets.append(wallet.values())
        #wallets.append(wallet)

    return wallets


def getNonce(address):
    mgsIp = '10.100.186.146:9207'
    url = f'http://{mgsIp}/v1/public/future/web3/get-nonce'
    headers = {'Content-Type': 'application/json', 'x-gray-env': 'lock'}
    data = json.dumps({'sourceAddr': address, 'type': "login"})
    res = requests.post(url=url, headers=headers, data=data)
    return res.json()['data']['nonce']


def generateSignature(nonce, privateKey):
    msg = 'You are signing into ApolloX Finance Trading '+nonce
    message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=privateKey)
    signature = w3.toHex(signed_message.signature)
    return signature


def saveETHWalletCsv(jsonData):
    with open('wallets.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["序号", "钱包地址", "私钥"])
        csv_writer.writerows(jsonData)


def saveETHWalletJson(jsonData):
    with open('test.json', 'w', newline='') as test_json:
        json.dump(jsonData, test_json)

# res = getNonce('0x6BdF6995bd0534Af5e6D92e6c8430F43c0BDd559')
# print(res)
# signature = generateSignature(getNonce('0x6BdF6995bd0534Af5e6D92e6c8430F43c0BDd559'), '9867eed2eef0d243573134179798608221e039c138ca19c211c8c4a2b9594042')
# print(signature)


wallets = createNewETHWallet()
# print(wallets)
# walletsJson = []
# for wallet in wallets:
#     wallet['nonce'] = getNonce(wallet['address'])
#     signature = generateSignature(wallet['nonce'], wallet['privateKey'])
#     wallet['signature'] = signature
#     walletsJson.append(wallet.values())

saveETHWalletCsv(wallets)
# saveETHWalletJson(wallets)


