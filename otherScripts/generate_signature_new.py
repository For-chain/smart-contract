from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3
from eth_abi import encode
from config import *


# 编码函数，生成原始的 bytes message
def encode_message(exchange_rate_info_list, uint256_1, uint256_2):
    # 编码 ExchangeRateInfo[]，首先编码每个结构体
    encoded_structs = b"".join([
        encode(
            ["address", "uint256", "uint256"],
            [
                info["assTokenAddress"],
                info["assToSourceExchangeRate"],
                info["exchangeRateExpiredTimestamp"]
            ]
        )
        for info in exchange_rate_info_list
    ])

    # 将完整的数组长度和数据部分编码
    encoded_message = encode(
        ["bytes", "uint256", "uint256"],
        [encoded_structs, uint256_1, uint256_2]
    )

    return encoded_message


def modify_data(original_data, line_number, new_value):
    # 将原始数据按每64个字符分割为行
    data_lines = [original_data[i:i + 64] for i in range(0, len(original_data), 64)]
    # print("data_lines:", data_lines)

    # 确保 line_number 在有效范围内
    if line_number < 0 or line_number >= len(data_lines):
        raise ValueError(f"Invalid line number: {line_number}")

    # 替换指定行
    data_lines[line_number] = new_value

    # 将修改后的数据行重新拼接为一个字符串
    modified_data = "".join(data_lines)

    return bytes.fromhex(modified_data)


# 签名函数
def sign_message(private_key, exchange_rate_info_list, uint256_1, uint256_2):
    encoded_message = encode_message(exchange_rate_info_list, uint256_1, uint256_2)
    print("Encoded bytes message:", encoded_message.hex())  # 打印原始bytes
    # print(type(encoded_message))
    #直接生成的编码没有按照偏移量指定数组变量位置，没有想到好的办法解决，只能人工替换
    modified_message = modify_data(encoded_message.hex(), 3, "0000000000000000000000000000000000000000000000000000000000000001")
    print("Modified data:", '0x'+ modified_message.hex())
    # print(type(modified_message))
    message_hash = Web3.keccak(modified_message)  # 对原始 bytes 进行 Keccak256
    print("message_hash:", message_hash.hex())
    message_defunct = encode_defunct(hexstr=message_hash.hex())  # 封装为 eth_sign 格式
    print("message_defunct:", message_defunct)
    signed_message = Account.sign_message(message_defunct, private_key=private_key)
    return signed_message.signature


# 示例数据 asBTC合约uploadExchangeRate入参
private_key = WALLET_PRIVATE_KEY_1  # 替换为实际私钥
exchange_rate_info_list = [
    {
        "assTokenAddress": "0x9995A3B5881A9D6Eaea16d41db9e26EFc1801F64",
        "assToSourceExchangeRate": 103000000,
        "exchangeRateExpiredTimestamp": 1732935025
    }
]
uint256_1 = 1732157425
uint256_2 = 97

signature = sign_message(private_key, exchange_rate_info_list, uint256_1, uint256_2)
print("Signature:", signature.hex())
