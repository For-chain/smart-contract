from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3
from config import *


# 编码函数，处理 ExchangeRateInfo[] 和 uint256
def encode_message(exchange_rate_info_list, uint256_1, uint256_2):
    # 对ExchangeRateInfo[]中的每个struct单独编码
    struct_hashes = [
        Web3.solidity_keccak(
            ["address", "uint256", "uint256"],
            [
                info["assTokenAddress"],
                info["assToSourceExchangeRate"],
                info["exchangeRateExpiredTimestamp"]
            ]
        )
        for info in exchange_rate_info_list
    ]

    # 将所有的struct_hash拼接起来后再hash
    combined_struct_hash = Web3.solidity_keccak(["bytes32"] * len(struct_hashes), struct_hashes)

    # 最终消息hash，包括两个uint256
    message_hash = Web3.solidity_keccak(
        ["bytes32", "uint256", "uint256"],
        [combined_struct_hash, uint256_1, uint256_2]
    )

    return message_hash


# 签名函数
def sign_message(private_key, exchange_rate_info_list, uint256_1, uint256_2):
    message_hash = encode_message(exchange_rate_info_list, uint256_1, uint256_2)
    message = encode_defunct(hexstr=message_hash.hex())  # 用 eth_sign 格式封装消息
    signed_message = Account.sign_message(message, private_key=private_key)
    return signed_message.signature


# 示例数据
private_key = WALLET_PRIVATE_KEY_1  # 替换为实际私钥
exchange_rate_info_list = [
    {
        "assTokenAddress": "0x9995A3B5881A9D6Eaea16d41db9e26EFc1801F64",
        "assToSourceExchangeRate": 100001010,
        "exchangeRateExpiredTimestamp": 1732071026
    }
]
uint256_1 = 1732081026
uint256_2 = 97

signature = sign_message(private_key, exchange_rate_info_list, uint256_1, uint256_2)
print("Signature:", signature.hex())
