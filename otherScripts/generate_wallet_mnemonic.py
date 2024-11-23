import csv
from mnemonic import Mnemonic
from eth_account import Account
from eth_utils import to_checksum_address

# 启用未审核的助记词功能
Account.enable_unaudited_hdwallet_features()

def generate_wallets(mnemonic_phrase, num_wallets, derivation_path="m/44'/60'/0'/0/"):
    """
    生成以太坊钱包地址和私钥。

    :param mnemonic_phrase: 助记词（12或24个单词）
    :param num_wallets: 要生成的钱包数量
    :param derivation_path: BIP-44衍生路径，默认为以太坊路径 m/44'/60'/0'/0/
    :return: 钱包地址和私钥的列表
    """
    mnemo = Mnemonic("english")
    if not mnemo.check(mnemonic_phrase):
        raise ValueError("Invalid mnemonic phrase.")

    wallets = []
    for i in range(num_wallets):
        # 获取当前衍生路径
        path = f"{derivation_path}{i}"
        # 根据助记词和衍生路径生成种子
        seed = mnemo.to_seed(mnemonic_phrase)
        # 创建账户对象
        account = Account.from_mnemonic(mnemonic_phrase, account_path=path)
        # 转换地址为 EIP-55 检查地址格式
        address = to_checksum_address(account.address)
        wallets.append({"address": address, "private_key": account.key.hex()})

    return wallets


def save_wallets_to_csv(wallets, filename="wallets_mnemonic.csv"):
    """
    将钱包地址和私钥保存到 CSV 文件。

    :param wallets: 包含地址和私钥的列表
    :param filename: CSV 文件名
    """
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["address", "private_key"])
        writer.writeheader()
        writer.writerows(wallets)
    print(f"Wallets saved to {filename}")


# 示例用法
mnemonic = "foil pony urban news tobacco struggle damp dash cook expect diary hello"  # 替换为你的助记词
num_wallets = 32  # 需要生成的钱包数量

wallets = generate_wallets(mnemonic, num_wallets)
# for i, wallet in enumerate(wallets):
#     print(f"Wallet {i + 1}:")
#     print(f"  Address: {wallet['address']}")
#     print(f"  Private Key: {wallet['private_key']}")

save_wallets_to_csv(wallets, filename="wallets_mnemonic.csv")
print("Wallets have been saved to wallets.csv")