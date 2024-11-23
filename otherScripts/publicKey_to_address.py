from eth_utils import keccak
from eth_utils import to_checksum_address

# 公钥
public_key = "03b2cd157ca5936b87a3e5e11717141592b2261b9d68bab8d5cf3695ff52a9dd18"

# 将公钥转换为字节
public_key_bytes = bytes.fromhex(public_key)

# 计算公钥的 Keccak-256 哈希值
keccak_hash = keccak(public_key_bytes)  # 去掉公钥的前缀 0x04

# 获取最后20字节作为地址
address = to_checksum_address(keccak_hash[-20:])

print("Address:", address)
