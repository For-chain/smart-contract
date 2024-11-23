from web3 import Web3, HTTPProvider
from eth_utils import keccak
from config import *

w3 = Web3(HTTPProvider(BSC_RPC_URL_MAIN))

contract_address = BSC_APOLLOX_CONTRACT_MAIN
slot_position = "apollox.swap.manager.storage"
# slot_position = 0

# 计算数组元素的存储槽位置
# slot = w3.to_hex(keccak(text=slot_position).rjust(32, b'\x00'))

slot = w3.to_hex(keccak(text=slot_position))

# 读取数组中第 i 个元素的数据
storage_data = w3.eth.get_storage_at(contract_address, slot)
print(f"origin data: {storage_data}")
# 地址变量转换
address = w3.to_checksum_address(storage_data.hex()[-40:])
print(f"Decoded address: {address}")

# unit256或int256类型转换
# value = int(storage_data.hex(), 16)
# print(f"Decoded uint256 value: {value}")

# bool类型转换
# bool_value = bool(int(storage_data.hex(), 16))
# print(f"Decoded boolean value: {bool_value}")


