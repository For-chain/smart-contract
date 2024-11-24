import base58

# 假设字符串为 Base58 编码
base58_string = "HnKeu9xPP9dFt16Kcj4kDZEUwetSNKM8TcuzZtoPSqSq"
decoded_bytes = base58.b58decode(base58_string)
hex_result = '0x'+str(decoded_bytes.hex())

print("Base58 解码后转为16进制:", hex_result)


