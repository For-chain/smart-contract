import base58

# 原始十六进制字符串
hex_string = "f95737ff13516f41091ef6a149319be07981aa89d86384d5bf2d06b0b4e06862"

# 将十六进制字符串转换为二进制数据
binary_data = bytes.fromhex(hex_string)

# 使用 Base58 编码
base58_encoded = base58.b58encode(binary_data)

print("Base58 编码结果:", base58_encoded.decode())
