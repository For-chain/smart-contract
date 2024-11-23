# 负数转换

hex_string = "0xfffffffffffffffffffffffffffffffffffffffffffffffc775c8ddd8d352663"
decimal_number = int(hex_string, 16) - 2**256
print(decimal_number)