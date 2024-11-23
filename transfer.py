from eth_account import Account
from web3 import Web3, HTTPProvider
from config import *
import account
from tokens.abi import ERC20_abi

w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))


def transfer_eth(privateKey, nonce, from_address, target_address, amount):
    params = {
        'nonce': nonce,
        'to': target_address,
        'value': w3.to_wei(amount, 'ether'),
        'gas': 300000,
        'gasPrice': w3.to_wei('15', 'gwei'),
        'from': from_address,
    }
    signed_tx = w3.eth.account.signTransaction(params, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)


def transfer_erc20(privateKey, nonce, recipient, amount, tokenContract):
    params = {
        'gas': 300000,
        'gasPrice': w3.to_wei('15', 'gwei'),
        'nonce': nonce,
    }
    func = tokenContract.functions.transfer(recipient, w3.to_wei(amount, 'ether'))
    tx = func.build_transaction(params)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)


if __name__ == '__main__':
    bscTestnetBUSD = w3.eth.contract(address=BSC_BUSD_TOKEN_TEST, abi=ERC20_abi.abi)
    bscTestnetUSDT = w3.eth.contract(address=BSC_USDT_TOKEN_TEST, abi=ERC20_abi.abi)
    tokenContracts = [bscTestnetBUSD, bscTestnetUSDT]

    nonce = w3.eth.get_transaction_count(TREASURY_ADDRESS)
    w3 = Web3(HTTPProvider(BSC_RPC_URL_TEST))
    accountList = account.generateAccountFromMnemonic('foil pony urban news tobacco struggle damp dash cook expect diary hello', 10)

    for address in accountList.keys():
        for token in tokenContracts:
            transfer_erc20(TREASURY_KEY, nonce, address, 10000, token)
            print(nonce)
            nonce = nonce + 1
