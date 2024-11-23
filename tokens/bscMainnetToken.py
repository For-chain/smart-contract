import sys
import os

from tokens.abi import ERC20_abi
from web3 import Web3, HTTPProvider
from tokens.contract import Erc20
from config import *

w3 = Web3(HTTPProvider(BSC_RPC_URL_MAIN))

transfer_tokens = [BSC_BUSD_MAIN, BSC_USDT_MAIN, BSC_APX_MAIN, BSC_CAKE_MAIN, BSC_BABY_MAIN, BSC_USDC_MAIN, BSC_BANANA_MAIN, BSC_VUSDT_MAIN, BSC_MDX_MAIN, BSC_HAY_MAIN, BSC_BSW_MAIN]

old_contract = '0xe2e912F0b1b5961be7CB0D6dbb4A920ACe06Cd99'
new_contract = '0xcEF2dD45Da08b37fB1c2f441d33c2eBb424866A4'

for item in transfer_tokens:
    token = w3.eth.contract(address=item, abi=ERC20_abi.abi)
    erc20 = Erc20.Erc20(w3, token, BSC_GWEI_MAIN)
    print("isETH: false")
    print("currency: " + item)
    print("amount: " + str(erc20.balanceOf(old_contract)))
    print("\n")



