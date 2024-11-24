import logging
import csv
import random
import time
from binance.spot import Spot
from binance.lib.utils import config_logging
from secret import *


def get_wallet_addresses_from_csv(file_path, request_count):
    """
    从 CSV 文件中读取钱包地址。

    :param file_path: CSV 文件路径
    :param request_count: 请求数量，表示需要多少个钱包地址
    :return: 返回钱包地址列表
    """
    wallet_addresses = []

    # 读取 CSV 文件
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        # 跳过第一行（表头）
        next(reader)
        for row in reader:
            # 假设每行的格式是 [wallet_address, wallet_privatekey]
            wallet_address = row[0]
            wallet_addresses.append(wallet_address)

            # 如果已经取到所需数量，提前返回
            if len(wallet_addresses) >= request_count:
                break

    return wallet_addresses

def muti_withdraw_from_binance(wallets, amount):
    # 随机处理amount数值
    random_amount = lambda number: round(number * random.uniform(0.950, 1.050), 4)
    config_logging(logging, logging.INFO)

    # client = Spot()
    # logging.info(client.time())

    client = Spot(api_key=API_KEY_SELF, api_secret=API_SECRET_SELF)

    for i, address in enumerate(wallets):
        params = {
            'coin': 'ETH',
            'address': address,
            'network': 'base',
            'amount': random_amount(amount),
            'walletType': 0
        }
        logging.info(client.time())
        print(f"excute {i}: {params}")
        #调用binance api
        response = client.withdraw(**params)
        logging.info(response)
        time.sleep(0.2)

if __name__ == "__main__":
    # 假设 CSV 文件路径为 'wallets.csv'，请求数量为 5
    file_path = 'wallets_mnemonic.csv'
    request_count = 2

    wallets = get_wallet_addresses_from_csv(file_path, request_count)
    # 检查钱包地址正确
    for i, wallet in enumerate(wallets):
        print(f"wallet {i}: {wallet}")

    muti_withdraw_from_binance(wallets, 0.02)