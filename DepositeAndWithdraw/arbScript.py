import sys
import os

sys.path.append("../../chainlink")

from DepositeAndWithdraw.contract import ArbTreasury
from web3 import Web3, HTTPProvider
from config import *
from tokens.abi import ERC20_abi

w3 = Web3(HTTPProvider(ARB_RPC_URL_TEST))
nonce_1 = w3.eth.get_transaction_count(WALLET_ADDRESS_1)

message = '0x000000000000000000000000000000000000000000000000096fce767b901000000000000000000000000000e90f9596e3bfd49e9f4c2e0ea48830dc47e6997b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000cadbdbca048ba092f7ee61a5795e17463544dc0000000000000000000000000000000000000000000000000000000000000003d40000000000000000000000000000000000000000000000000000000063f343a5'
signature = '0x350ab1138626fa4b3e2773cdc9ace8ec5606233d558d87ebb1add9c591992e056b398fbcda786d766736a2e4ee662546413a264d8c08d2539fd50c5b039619581b'


ArbTreasury.claim(WALLET_PRIVATE_KEY_1, nonce_1, message, signature)
ArbTreasury.withdraw(WALLET_PRIVATE_KEY_1, nonce_1+1, message, signature)


