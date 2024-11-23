from web3 import Web3

# Method signature string
method_signature = "slot0(uint160,int24,uint16,uint16,uint16,uint32,bool)"

# Compute the Keccak-256 hash of the method signature and take the first 4 bytes
method_selector = Web3.keccak(text=method_signature)[:4]

# Convert to hex
method_selector_hex = method_selector.hex()

print(method_selector_hex)
