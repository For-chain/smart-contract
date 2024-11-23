from eth_account import Account
from web3 import Web3, HTTPProvider
from config import *

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))

def generateAccountFromMnemonic(mnemonic, number):
    account = {}
    Account.enable_unaudited_hdwallet_features()
    iterator = 0
    for i in range(number):
        acct = Account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{iterator}")
        account[acct.address] = acct.key
        iterator = iterator + 1
    return account


# account = generateAccountFromMnemonic('foil pony urban news tobacco struggle damp dash cook expect diary hello', 10)

